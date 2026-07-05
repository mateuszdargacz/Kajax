from django.db.models import Q


SMOKE_QUERY_PARAM = "kajax_smoke"
SMOKE_TEST_NAME = "Lead E2E"
SMOKE_TEST_PHONE = "604000000"
SMOKE_ADMIN_NOTE_PREFIX = "Automatyczny smoke test produkcji"
SMOKE_ADMIN_NOTE = (
    f"{SMOKE_ADMIN_NOTE_PREFIX}. Powiadomienia email zostaly celowo pominiete; "
    "rekord moze zostac usuniety przez cleanup-prod-smoke-leads.sh."
)


def is_smoke_quote_request(request, quote_request):
    return (
        request.GET.get(SMOKE_QUERY_PARAM) == "1"
        and quote_request.name == SMOKE_TEST_NAME
        and quote_request.phone == SMOKE_TEST_PHONE
    )


def mark_smoke_quote_request(quote_request):
    note = quote_request.admin_notes.strip()
    if SMOKE_ADMIN_NOTE_PREFIX not in note:
        quote_request.admin_notes = f"{note}\n{SMOKE_ADMIN_NOTE}".strip()
        quote_request.save(update_fields=["admin_notes", "updated_at"])


def smoke_cleanup_queryset():
    from leads.models import QuoteRequest

    return QuoteRequest.objects.filter(
        Q(name=SMOKE_TEST_NAME, phone=SMOKE_TEST_PHONE)
        | Q(admin_notes__contains=SMOKE_ADMIN_NOTE_PREFIX)
    )
