from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.translation import get_language
from django.views.generic.edit import FormView

from leads.copy import get_form_copy
from leads.email import send_quote_emails
from leads.forms import QuoteRequestForm
from leads.models import QuoteAttachment
from leads.piecode_sync import sync_quote_request_to_piecode
from pages.content import get_page_content
from pages.views import build_seo_context


INQUIRY_BUSINESS_LINES = {
    "b2b_components": "b2b_wooden_components",
    "construction_joinery": "construction_joinery",
    "custom_artistic": "custom_architectural_details",
    "other": "mixed",
}


class QuoteRequestView(FormView):
    form_class = QuoteRequestForm
    template_name = "pages/quote.html"
    success_url = reverse_lazy("quote")

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["language_code"] = get_language() or "pl"
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        language = get_language()
        page = get_page_content("quote", language)
        context["page"] = page
        context.update(build_seo_context(page, language))
        context["quote_success_event"] = self.request.session.pop("quote_success_event", None)
        return context

    def form_valid(self, form):
        quote_request = form.save(commit=False)
        quote_request.language = get_language() or ""
        quote_request.source_path = self.request.path
        quote_request.user_agent = self.request.META.get("HTTP_USER_AGENT", "")
        quote_request.save()

        for uploaded_file in form.cleaned_data.get("attachments", []):
            QuoteAttachment.objects.create(
                quote_request=quote_request,
                file=uploaded_file,
                original_name=uploaded_file.name,
            )

        send_quote_emails(quote_request)
        sync_quote_request_to_piecode(quote_request, self.request)
        self.request.session["quote_success_event"] = {
            "quote_id": quote_request.pk,
            "lead_type": "quote_request",
            "project_type": quote_request.inquiry_type,
            "business_line": INQUIRY_BUSINESS_LINES.get(quote_request.inquiry_type, "mixed"),
        }
        messages.success(self.request, get_form_copy(quote_request.language)["success_message"])
        return redirect(self.get_success_url())
