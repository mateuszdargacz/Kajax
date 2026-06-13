from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.translation import get_language
from django.views.generic.edit import FormView

from leads.copy import get_form_copy
from leads.email import send_quote_emails
from leads.forms import QuoteRequestForm
from leads.models import QuoteAttachment
from pages.content import get_page_content
from pages.views import build_seo_context


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
        messages.success(self.request, get_form_copy(quote_request.language)["success_message"])
        return redirect(self.get_success_url())
