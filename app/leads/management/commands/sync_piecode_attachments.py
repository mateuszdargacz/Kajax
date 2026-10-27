import json
from urllib.parse import urlsplit, urlunsplit

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError

from leads.models import QuoteRequest
from leads.piecode_sync import attachment_items, post_json


class Command(BaseCommand):
    help = "Refresh attachment references of already synced leads; no email or new lead."

    def add_arguments(self, parser):
        parser.add_argument("--quote-id", type=int, action="append")
        parser.add_argument("--apply", action="store_true")

    def handle(self, *args, **options):
        source = urlsplit(settings.PIECODE_LEAD_SYNC_LEAD_URL)
        if source.scheme != "https" or source.hostname not in {"piecode.pl", "api.piecode.pl", "www.piecode.pl"}:
            raise CommandError("piecode_sync_target_invalid")
        endpoint = urlunsplit((source.scheme, source.netloc, "/api/leads/source-attachments", "", ""))
        quotes = QuoteRequest.objects.exclude(central_lead_id="").prefetch_related("attachments").order_by("pk")
        if options["quote_id"]:
            quotes = quotes.filter(pk__in=options["quote_id"])
        reports = []
        for quote in quotes:
            attachments = attachment_items(quote)
            if not attachments:
                continue
            report = {"quote_id": quote.pk, "attachments": len(attachments), "updated": False}
            if options["apply"]:
                try:
                    result = post_json(endpoint, {"lead_id": quote.central_lead_id,
                        "workspace_id": "kajax", "local_quote_id": str(quote.pk), "attachments": attachments})
                except Exception:
                    raise CommandError(f"attachment_sync_failed_quote_{quote.pk}") from None
                if not result.get("ok"):
                    raise CommandError(f"attachment_sync_rejected_quote_{quote.pk}")
                report["updated"] = True
            reports.append(report)
        self.stdout.write(json.dumps({"email_sent": False, "leads_created": False, "quotes": reports}))
