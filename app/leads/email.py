import logging
import mimetypes
from pathlib import Path

from django.conf import settings
from django.core.mail import EmailMultiAlternatives
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
    html_body = render_to_string(
        "emails/quote_notification.html",
        {"quote": quote_request, "notification": NOTIFICATION_COPY, "display": display},
    )
    reply_to = [quote_request.email] if quote_request.email else None
    _send(
        subject,
        body,
        recipients,
        html_body=html_body,
        reply_to=reply_to,
        attachments=_notification_attachments(quote_request),
    )


def _send_requester_confirmation(quote_request):
    if not quote_request.email:
        return
    copy = get_confirmation_copy(quote_request.language)
    body = render_to_string(
        "emails/quote_confirmation.txt",
        {"quote": quote_request, "confirmation": copy, "display": get_quote_display(quote_request, quote_request.language)},
    )
    html_body = render_to_string(
        "emails/quote_confirmation.html",
        {"quote": quote_request, "confirmation": copy, "display": get_quote_display(quote_request, quote_request.language)},
    )
    subject = copy["subject"]
    _send(subject, body, [quote_request.email], html_body=html_body)


def _send(subject, body, recipients, html_body=None, reply_to=None, attachments=None):
    try:
        email = EmailMultiAlternatives(
            subject=subject,
            body=body,
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=recipients,
            reply_to=reply_to,
        )
        if html_body:
            email.attach_alternative(html_body, "text/html")
        for filename, content, mimetype in attachments or []:
            email.attach(filename, content, mimetype)
        email.send(fail_silently=False)
    except Exception:
        if settings.LEAD_EMAIL_FAIL_SILENTLY:
            logger.exception("Failed to send quote email.")
            return
        raise


def _notification_attachments(quote_request):
    for attachment in quote_request.attachments.all():
        if not attachment.file:
            continue
        filename = Path(attachment.original_name or attachment.file.name).name or "zalacznik"
        try:
            with attachment.file.open("rb") as file_handle:
                content = file_handle.read()
        except (FileNotFoundError, OSError, ValueError):
            logger.exception(
                "Skipping missing quote attachment %s for Kajax quote %s.",
                attachment.pk,
                quote_request.pk,
            )
            continue
        content_type = mimetypes.guess_type(filename)[0] or "application/octet-stream"
        yield filename, content, content_type


def get_quote_display(quote_request, language_code):
    copy = get_form_copy(language_code)
    return {
        "inquiry_type": copy.get(quote_request.inquiry_type, quote_request.get_inquiry_type_display()),
        "scale": copy.get(quote_request.scale or "unknown", quote_request.get_scale_display()),
    }
