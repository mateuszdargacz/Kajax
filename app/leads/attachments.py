from pathlib import Path

from django.core import signing
from django.http import FileResponse, Http404
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_safe

from leads.models import QuoteAttachment


GRANT_SALT = "kajax.piecode.quote-attachment.v1"


def attachment_grant(attachment):
    # Bound to this stored file; never put this capability in a URL or an admin projection.
    return signing.Signer(salt=GRANT_SALT).sign_object({
        "attachment": attachment.pk,
        "quote": attachment.quote_request_id,
        "file": attachment.file.name,
    })


def attachment_response(attachment):
    try:
        handle = attachment.file.open("rb")
    except (OSError, ValueError):
        raise Http404 from None
    response = FileResponse(
        handle, as_attachment=True,
        filename=Path(attachment.original_name or attachment.file.name).name,
    )
    response["Cache-Control"] = "private, no-store"
    response["X-Content-Type-Options"] = "nosniff"
    return response


@require_safe
def source_attachment(request, attachment_id):
    grant = request.headers.get("X-Piecode-Attachment-Grant", "")
    if not grant or len(grant) > 4096:
        raise Http404
    try:
        binding = signing.Signer(salt=GRANT_SALT).unsign_object(grant)
    except (signing.BadSignature, ValueError, TypeError):
        raise Http404 from None
    if not isinstance(binding, dict) or binding.get("attachment") != attachment_id:
        raise Http404
    attachment = get_object_or_404(
        QuoteAttachment.objects.select_related("quote_request"),
        pk=attachment_id, quote_request_id=binding.get("quote"), file=binding.get("file"),
    )
    response = attachment_response(attachment)
    response["X-Piecode-Lead-ID"] = attachment.quote_request.central_lead_id
    response["X-Kajax-Quote-ID"] = str(attachment.quote_request_id)
    return response
