from unittest.mock import patch

from django.core import mail
from django.test import TestCase, override_settings
from django.urls import reverse

from leads.models import QuoteRequest


@override_settings(
    EMAIL_BACKEND="django.core.mail.backends.locmem.EmailBackend",
    LEAD_RECIPIENTS=["mail@kajax.eu", "mateuszdargacz@gmail.com", "kajax-stolarstwo@o2.pl"],
    DEFAULT_FROM_EMAIL="Kajax Stolarstwo <mail@kajax.eu>",
)
class QuoteRequestTests(TestCase):
    def test_quote_form_creates_lead_and_sends_emails(self):
        response = self.client.post(
            reverse("quote"),
            {
                "name": "Test Lead",
                "email": "lead@example.com",
                "phone": "123456789",
                "company": "Example Company",
                "inquiry_type": QuoteRequest.InquiryType.B2B_COMPONENTS,
                "scale": QuoteRequest.Scale.SMALL_SERIES,
                "location": "Gdańsk / Europe",
                "expected_timing": "Q3",
                "message": "Potrzebujemy krótkiej serii elementów według rysunku.",
                "consent": "on",
            },
        )

        self.assertEqual(response.status_code, 302)
        self.assertEqual(QuoteRequest.objects.count(), 1)
        self.assertEqual(len(mail.outbox), 2)
        self.assertEqual(mail.outbox[0].to, ["mail@kajax.eu", "mateuszdargacz@gmail.com", "kajax-stolarstwo@o2.pl"])
        self.assertEqual(mail.outbox[0].reply_to, ["lead@example.com"])
        self.assertEqual(mail.outbox[0].from_email, "Kajax Stolarstwo <mail@kajax.eu>")
        self.assertEqual(mail.outbox[0].alternatives[0][1], "text/html")
        self.assertIn("Nowe zapytanie ze strony", mail.outbox[0].alternatives[0][0])
        self.assertEqual(mail.outbox[1].to, ["lead@example.com"])
        self.assertEqual(mail.outbox[1].alternatives[0][1], "text/html")

        quote = QuoteRequest.objects.get()
        self.assertEqual(quote.email, "lead@example.com")
        self.assertEqual(quote.inquiry_type, QuoteRequest.InquiryType.B2B_COMPONENTS)
        self.assertEqual(
            self.client.session["quote_success_event"],
            {
                "lead_type": "quote_request",
                "project_type": QuoteRequest.InquiryType.B2B_COMPONENTS,
                "business_line": "b2b_wooden_components",
            },
        )

    def test_quote_form_accepts_phone_without_email(self):
        response = self.client.post(
            reverse("quote"),
            {
                "name": "Lead Telefoniczny",
                "phone": "123456789",
                "inquiry_type": QuoteRequest.InquiryType.CONSTRUCTION_JOINERY,
                "message": "Chcę zapytać o schody drewniane.",
                "consent": "on",
            },
        )

        self.assertEqual(response.status_code, 302)
        self.assertEqual(QuoteRequest.objects.count(), 1)
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].to, ["mail@kajax.eu", "mateuszdargacz@gmail.com", "kajax-stolarstwo@o2.pl"])
        self.assertEqual(mail.outbox[0].reply_to, [])

        quote = QuoteRequest.objects.get()
        self.assertEqual(quote.email, "")
        self.assertEqual(quote.phone, "123456789")
        self.assertEqual(quote.scale, QuoteRequest.Scale.UNKNOWN)

    @override_settings(
        PIECODE_LEAD_SYNC_ENABLED=True,
        PIECODE_LEAD_SYNC_LEAD_URL="https://piecode.example/api/leads",
        PIECODE_LEAD_SYNC_EVENT_URL="https://piecode.example/api/events",
    )
    @patch("leads.piecode_sync.post_json")
    def test_quote_form_syncs_central_event_and_lead_after_success(self, post_json):
        post_json.side_effect = [
            {"ok": True, "accepted": 1},
            {"ok": True, "id": "central-123", "status": "new"},
        ]

        response = self.client.post(
            f"{reverse('quote')}?utm_source=google&utm_medium=cpc&utm_campaign=kajax_test&gclid=test-click-id",
            {
                "name": "Paid Lead",
                "email": "lead@example.com",
                "phone": "123456789",
                "company": "Example Company",
                "inquiry_type": QuoteRequest.InquiryType.B2B_COMPONENTS,
                "scale": QuoteRequest.Scale.SMALL_SERIES,
                "message": "Potrzebujemy krótkiej serii elementów według rysunku.",
                "consent": "on",
            },
        )

        self.assertEqual(response.status_code, 302)
        quote = QuoteRequest.objects.get(name="Paid Lead")
        self.assertEqual(quote.central_sync_status, "synced")
        self.assertEqual(quote.central_lead_id, "central-123")
        self.assertEqual(post_json.call_count, 2)

        event_url, event_payload = post_json.call_args_list[0].args
        lead_url, lead_payload = post_json.call_args_list[1].args
        self.assertEqual(event_url, "https://piecode.example/api/events")
        self.assertEqual(lead_url, "https://piecode.example/api/leads")
        self.assertEqual(event_payload["workspace_id"], "kajax")
        self.assertEqual(event_payload["event_name"], "lead_form_capture")
        self.assertEqual(event_payload["params"]["gclid"], "test-click-id")
        self.assertEqual(lead_payload["workspace_id"], "kajax")
        self.assertEqual(lead_payload["gclid"], "test-click-id")
        self.assertEqual(lead_payload["last_utm_campaign"], "kajax_test")
