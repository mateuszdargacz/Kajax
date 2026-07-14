import json
import logging
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

from django.conf import settings
from django.utils import timezone

from leads.attribution import attribution_for_lead
from leads.smoke import is_smoke_quote_request


logger = logging.getLogger(__name__)


INQUIRY_LABELS = {
    "b2b_components": "Elementy drewniane B2B",
    "construction_joinery": "Stolarka budowlana",
    "custom_artistic": "Custom / stolarstwo artystyczne",
    "other": "Inne",
}


BUSINESS_LINES = {
    "b2b_components": "b2b_wooden_components",
    "construction_joinery": "construction_joinery",
    "custom_artistic": "custom_architectural_details",
    "other": "mixed",
}


SERVICE_AREAS = {
    "b2b_components": "poland_wide",
    "construction_joinery": "pomerania",
    "custom_artistic": "poland_pomerania",
    "other": "mixed",
}


def post_json(url, payload):
    body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
    request = Request(
        url,
        data=body,
        method="POST",
        headers={
            "Content-Type": "application/json",
            "User-Agent": "kajax-piecode-sync/1.1",
        },
    )
    with urlopen(request, timeout=settings.PIECODE_LEAD_SYNC_TIMEOUT_SECONDS) as response:
        response_body = response.read().decode("utf-8")
        if not response_body:
            return {}
        return json.loads(response_body)


def lead_interest(quote_request):
    return INQUIRY_LABELS.get(quote_request.inquiry_type, quote_request.inquiry_type or "Zapytanie ofertowe")


def attachment_items(quote_request):
    items = []
    for attachment in quote_request.attachments.all():
        if not attachment.file:
            continue
        filename = Path(attachment.original_name or attachment.file.name).name
        if not filename:
            continue
        item = {"filename": filename}
        try:
            item["size"] = attachment.file.size
        except (OSError, ValueError):
            pass
        items.append(item)
    return items


def lead_message(quote_request):
    attachment_names = [item["filename"] for item in attachment_items(quote_request)]
    parts = [
        quote_request.message,
        "",
        "Dane zakresu:",
        f"- Typ: {lead_interest(quote_request)}",
        f"- Skala: {quote_request.scale or '-'}",
        f"- Firma: {quote_request.company or '-'}",
        f"- Lokalizacja: {quote_request.location or '-'}",
        f"- Termin: {quote_request.expected_timing or '-'}",
        f"- Telefon: {quote_request.phone or '-'}",
    ]
    if attachment_names:
        parts.append(f"- Załączniki: {', '.join(attachment_names)}")
    return "\n".join(parts).strip()


def is_dev_submission(quote_request, request):
    return request.GET.get("piecode_dev") == "1" or is_smoke_quote_request(request, quote_request)


def dev_submission_params(quote_request, request):
    if not is_dev_submission(quote_request, request):
        return {}
    return {
        "is_test": True,
        "environment": "dev",
        "test_source": "kajax_smoke" if is_smoke_quote_request(request, quote_request) else "piecode_dev",
    }


def event_payload(quote_request, request, attribution):
    business_line = BUSINESS_LINES.get(quote_request.inquiry_type, "mixed")
    service_area = SERVICE_AREAS.get(quote_request.inquiry_type, "mixed")
    params = {
        **attribution,
        **dev_submission_params(quote_request, request),
        "lead_type": "quote_request",
        "project_type": quote_request.inquiry_type,
        "business_line": business_line,
        "service_area": service_area,
        "inquiry_type": quote_request.inquiry_type,
        "scale": quote_request.scale,
        "attachment_count": quote_request.attachments.count(),
        "locale": quote_request.language or "pl",
        "lead_source": "kajax-quote-form",
        "page_type": "quote",
        "page_key": "quote",
    }
    return {
        "event_name": "generate_lead",
        "event_id": f"kajax-quote-{quote_request.pk}-generate-lead",
        "workspace_id": settings.PIECODE_WORKSPACE_ID,
        "page_path": request.get_full_path()[:400],
        "occurred_at": timezone.now().isoformat(),
        "params": params,
    }


def lead_payload(quote_request, request, attribution):
    attachments = attachment_items(quote_request)
    payload = {
        **attribution,
        **dev_submission_params(quote_request, request),
        "workspace_id": settings.PIECODE_WORKSPACE_ID,
        "form_name": "kajax-quote-request",
        "local_quote_id": str(quote_request.pk),
        "name": quote_request.name,
        "email": quote_request.email,
        "phone": quote_request.phone,
        "company": quote_request.company,
        "interest": lead_interest(quote_request),
        "message": lead_message(quote_request),
        "locale": quote_request.language or "pl",
        "page_path": request.get_full_path()[:500],
        "lead_source": "kajax-quote-form",
        "landing_variant": quote_request.inquiry_type or "quote",
        "privacy_acknowledged": True,
        "privacy_notice_version": "kajax-contact-consent-2026-06",
        "marketing_opt_in": False,
        "submitted_at": timezone.now().isoformat(),
    }
    if attachments:
        payload["attachment_count"] = len(attachments)
        payload["attachments"] = attachments
        payload["attachment_names"] = [item["filename"] for item in attachments]
    return payload


def has_contact_details(quote_request):
    return bool(quote_request.email or quote_request.phone)


def mark_sync(quote_request, status, central_lead_id="", error=""):
    quote_request.central_sync_status = status
    quote_request.central_lead_id = central_lead_id or quote_request.central_lead_id
    quote_request.central_sync_last_error = error[:2000]
    quote_request.central_synced_at = timezone.now() if status in {"synced", "event_only"} else None
    quote_request.save(
        update_fields=[
            "central_sync_status",
            "central_lead_id",
            "central_sync_last_error",
            "central_synced_at",
            "updated_at",
        ],
    )


def sync_quote_request_to_piecode(quote_request, request):
    if not settings.PIECODE_LEAD_SYNC_ENABLED:
        mark_sync(quote_request, "disabled")
        return {"ok": True, "status": "disabled"}

    attribution = attribution_for_lead(request)
    errors = []
    event_response = None
    lead_response = None

    if settings.PIECODE_LEAD_SYNC_EVENT_URL:
        try:
            event_response = post_json(settings.PIECODE_LEAD_SYNC_EVENT_URL, event_payload(quote_request, request, attribution))
        except (HTTPError, URLError, TimeoutError, OSError, ValueError) as error:
            errors.append(f"event_sync_failed: {error}")

    if settings.PIECODE_LEAD_SYNC_SEND_LEAD and has_contact_details(quote_request) and settings.PIECODE_LEAD_SYNC_LEAD_URL:
        try:
            lead_response = post_json(settings.PIECODE_LEAD_SYNC_LEAD_URL, lead_payload(quote_request, request, attribution))
        except (HTTPError, URLError, TimeoutError, OSError, ValueError) as error:
            errors.append(f"lead_sync_failed: {error}")

    if errors:
        error_text = " | ".join(errors)
        mark_sync(quote_request, "failed", error=error_text)
        logger.warning("Piecode central lead sync failed for Kajax quote %s: %s", quote_request.pk, error_text)
        return {"ok": False, "status": "failed", "errors": errors}

    central_lead_id = str(lead_response.get("id", "")) if isinstance(lead_response, dict) else ""
    if central_lead_id:
        mark_sync(quote_request, "synced", central_lead_id=central_lead_id)
        return {"ok": True, "status": "synced", "central_lead_id": central_lead_id}

    if event_response is not None:
        mark_sync(quote_request, "event_only")
        return {"ok": True, "status": "event_only"}

    mark_sync(quote_request, "skipped")
    return {"ok": True, "status": "skipped"}
