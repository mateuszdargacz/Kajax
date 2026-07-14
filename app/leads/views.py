from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.translation import get_language
from django.views.generic.edit import FormView

from leads.copy import get_form_copy
from leads.email import send_quote_emails
from leads.forms import QuoteRequestForm
from leads.models import QuoteAttachment
from leads.piecode_sync import dev_submission_params, sync_quote_request_to_piecode
from leads.smoke import is_smoke_quote_request, mark_smoke_quote_request
from pages.content import get_page_content
from pages.views import build_seo_context


INQUIRY_BUSINESS_LINES = {
    "b2b_components": "b2b_wooden_components",
    "construction_joinery": "construction_joinery",
    "custom_artistic": "custom_architectural_details",
    "other": "mixed",
}

INQUIRY_SERVICE_AREAS = {
    "b2b_components": "poland_wide",
    "construction_joinery": "pomerania",
    "custom_artistic": "poland_pomerania",
    "other": "mixed",
}


QUOTE_SEGMENTS = {
    "b2b": {
        "aliases": {"b2b", "produkcja", "production", "components", "serie"},
        "title": "B2B: rysunek, próbka albo krótka seria",
        "h1": "Wyślij rysunek, próbkę albo opis elementu do produkcji",
        "lead": "To ścieżka dla firm, które potrzebują drewnianego komponentu: profilu, listwy, elementu POS, półproduktu albo krótkiej serii do dalszego montażu. Najlepszy start to rysunek, wzór, zdjęcie, próbka lub krótka specyfikacja z liczbą sztuk.",
        "form_intro": "Napisz, co to za element, do czego będzie używany i ile sztuk ma powstać. Jeśli planujesz próbkę albo powtarzalne partie, dopisz to od razu.",
    },
    "pomorskie": {
        "aliases": {"pomorskie", "stolarka", "budowlanka", "construction", "schody", "drzwi"},
        "title": "Pomorskie: schody, drzwi, listwy i zabudowy",
        "h1": "Wyślij zdjęcia miejsca: schody, drzwi, listwy albo zabudowa",
        "lead": "To ścieżka dla lokalnej stolarki w Pomorskiem: schodów, drzwi, listew, progów, opasek, parapetów i zabudów na wymiar. Do pierwszej oceny wystarczą zdjęcia miejsca, miejscowość, orientacyjne wymiary i etap prac.",
        "form_intro": "Podaj miejscowość, co jest do wykonania, na jakim etapie jest budowa lub remont oraz telefon do szybkiego doprecyzowania.",
    },
    "custom": {
        "aliases": {"custom", "projekt", "detal", "architekt"},
        "title": "Projekt specjalny: detal, zabudowa albo element wnętrza",
        "h1": "Wyślij projekt, zdjęcie albo wzór drewnianego detalu",
        "lead": "To ścieżka dla detali pod projekt: zabudów, elementów wnętrz, lokali, ekspozycji i nietypowych części z drewna. Pokaż rysunek, inspirację, zdjęcie miejsca albo wzór do odtworzenia.",
        "form_intro": "Opisz efekt, który ma powstać, miejsce użycia i najważniejsze ograniczenia: wymiar, materiał, montaż, termin albo powtarzalność.",
    },
}


def normalize_quote_segment(raw_segment):
    value = (raw_segment or "").strip().lower()
    for segment, config in QUOTE_SEGMENTS.items():
        if value in config["aliases"]:
            return segment
    return ""


class QuoteRequestView(FormView):
    form_class = QuoteRequestForm
    template_name = "pages/quote.html"
    success_url = reverse_lazy("quote")

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["language_code"] = get_language() or "pl"
        kwargs["quote_segment"] = normalize_quote_segment(self.request.GET.get("segment"))
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        language = get_language()
        page = get_page_content("quote", language)
        quote_segment = normalize_quote_segment(self.request.GET.get("segment"))
        if quote_segment and language == "pl":
            segment_copy = QUOTE_SEGMENTS[quote_segment]
            page["h1"] = segment_copy["h1"]
            page["lead"] = segment_copy["lead"]
            page["form_intro"] = segment_copy["form_intro"]
        page["quote_paths"] = [path.copy() for path in page.get("quote_paths", [])]
        for path in page.get("quote_paths", []):
            path["url"] = f"{page['path']}?segment={'b2b' if 'B2B' in path['title'] else 'pomorskie'}"
            path["active"] = quote_segment and path["url"].endswith(f"segment={quote_segment}")
        context["page"] = page
        context["quote_segment"] = quote_segment
        context.update(build_seo_context(page, language))
        context["quote_success_event"] = self.request.session.pop("quote_success_event", None)
        return context

    def form_valid(self, form):
        quote_request = form.save(commit=False)
        quote_request.language = get_language() or ""
        quote_request.source_path = self.request.get_full_path()[:255]
        quote_request.user_agent = self.request.META.get("HTTP_USER_AGENT", "")
        quote_request.save()

        for uploaded_file in form.cleaned_data.get("attachments", []):
            QuoteAttachment.objects.create(
                quote_request=quote_request,
                file=uploaded_file,
                original_name=uploaded_file.name,
            )

        is_smoke = is_smoke_quote_request(self.request, quote_request)
        if is_smoke:
            mark_smoke_quote_request(quote_request)
        else:
            send_quote_emails(quote_request)
        sync_quote_request_to_piecode(quote_request, self.request)
        self.request.session["quote_success_event"] = {
            **dev_submission_params(quote_request, self.request),
            "quote_id": quote_request.pk,
            "lead_type": "quote_request",
            "project_type": quote_request.inquiry_type,
            "business_line": INQUIRY_BUSINESS_LINES.get(quote_request.inquiry_type, "mixed"),
            "service_area": INQUIRY_SERVICE_AREAS.get(quote_request.inquiry_type, "mixed"),
        }
        messages.success(self.request, get_form_copy(quote_request.language)["success_message"])
        return redirect(self.get_success_url())
