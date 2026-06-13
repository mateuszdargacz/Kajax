import logging

from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string

from leads.copy import get_form_copy
from leads.email_copy import NOTIFICATION_COPY, get_confirmation_copy


logger = logging.getLogger(__name__)


def send_quote_emails(quote_request):
    recipients = getattr(settings, "LEAD_RECIPIENTS", [])
    if recipients:
        _send_company_notification(quote_request, recipients)
    _send_requester_confirmation(quote_request)


def _send_company_notification(quote_request, recipients):
    display = get_quote_display(quote_request, "pl")
    subject = NOTIFICATION_COPY["subject"].format(inquiry_type=display["inquiry_type"])
    body = render_to_string(
        "emails/quote_notification.txt",
        {"quote": quote_request, "notification": NOTIFICATION_COPY, "display": display},
    )
    _send(subject, body, recipients)


def _send_requester_confirmation(quote_request):
    if not quote_request.email:
        return
    copy = get_confirmation_copy(quote_request.language)
    body = render_to_string(
        "emails/quote_confirmation.txt",
        {"quote": quote_request, "confirmation": copy, "display": get_quote_display(quote_request, quote_request.language)},
    )
    subject = copy["subject"]
    _send(subject, body, [quote_request.email])


def _send(subject, body, recipients):
    try:
        send_mail(
            subject=subject,
            message=body,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=recipients,
            fail_silently=False,
        )
    except Exception:
        if settings.LEAD_EMAIL_FAIL_SILENTLY:
            logger.exception("Failed to send quote email.")
            return
        raise


def get_quote_display(quote_request, language_code):
    copy = get_form_copy(language_code)
    return {
        "inquiry_type": copy.get(quote_request.inquiry_type, quote_request.get_inquiry_type_display()),
        "scale": copy.get(quote_request.scale or "unknown", quote_request.get_scale_display()),
    }
