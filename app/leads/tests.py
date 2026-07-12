import tempfile
from unittest.mock import patch

from django.core import mail
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase, override_settings
from django.urls import reverse

from leads.email import send_quote_emails
from leads.models import QuoteAttachment, QuoteRequest
from leads.smoke import SMOKE_ADMIN_NOTE_PREFIX, smoke_cleanup_queryset


@override_settings(
    EMAIL_BACKEND="django.core.mail.backends.locmem.EmailBackend",
    LEAD_RECIPIENTS=["mail@kajax.eu", "mateuszdargacz@gmail.com", "kajax-stolarstwo@o2.pl"],
    DEFAULT_FROM_EMAIL="Kajax Stolarstwo <mail@kajax.eu>",
)
class QuoteRequestTests(TestCase):
    def setUp(self):
        super().setUp()
        self.media_root = tempfile.TemporaryDirectory()
        self.addCleanup(self.media_root.cleanup)
        self.settings_override = override_settings(MEDIA_ROOT=self.media_root.name)
        self.settings_override.enable()
        self.addCleanup(self.settings_override.disable)

    def test_quote_form_creates_lead_and_sends_emails(self):
        response = self.client.post(
            f"{reverse('quote')}?segment=b2b&utm_campaign=test",
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
        self.assertEqual(mail.outbox[0].attachments, [])
        self.assertEqual(mail.outbox[0].alternatives[0][1], "text/html")
        self.assertIn("Nowe zapytanie ze strony", mail.outbox[0].alternatives[0][0])
        self.assertEqual(mail.outbox[1].to, ["lead@example.com"])
        self.assertEqual(mail.outbox[1].attachments, [])
        self.assertEqual(mail.outbox[1].alternatives[0][1], "text/html")

        quote = QuoteRequest.objects.get()
        self.assertEqual(quote.email, "lead@example.com")
        self.assertEqual(quote.inquiry_type, QuoteRequest.InquiryType.B2B_COMPONENTS)
        self.assertEqual(quote.source_path, "/wycena/?segment=b2b&utm_campaign=test")
        self.assertEqual(
            self.client.session["quote_success_event"],
            {
                "quote_id": quote.pk,
                "lead_type": "quote_request",
                "project_type": QuoteRequest.InquiryType.B2B_COMPONENTS,
                "business_line": "b2b_wooden_components",
                "service_area": "poland_wide",
            },
        )

    def test_quote_segments_preselect_relevant_inquiry_type(self):
        b2b_response = self.client.get(f"{reverse('quote')}?segment=b2b")
        pomorskie_response = self.client.get(f"{reverse('quote')}?segment=pomorskie")

        self.assertEqual(b2b_response.context["form"]["inquiry_type"].value(), QuoteRequest.InquiryType.B2B_COMPONENTS)
        self.assertEqual(b2b_response.context["form"]["scale"].value(), QuoteRequest.Scale.SMALL_SERIES)
        self.assertContains(b2b_response, "Wyślij rysunek, próbkę albo opis elementu do produkcji")
        self.assertContains(b2b_response, 'href="/wycena/?segment=b2b"')
        self.assertEqual(
            pomorskie_response.context["form"]["inquiry_type"].value(),
            QuoteRequest.InquiryType.CONSTRUCTION_JOINERY,
        )
        self.assertContains(pomorskie_response, "Wyślij zdjęcia miejsca: schody, drzwi, listwy albo zabudowa")
        self.assertContains(pomorskie_response, 'href="/wycena/?segment=pomorskie"')

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

    def test_quote_form_attaches_uploaded_files_to_company_notification_only(self):
        uploaded_file = SimpleUploadedFile(
            "rysunek-testowy.txt",
            b"testowy opis rysunku",
            content_type="text/plain",
        )

        response = self.client.post(
            reverse("quote"),
            {
                "name": "Lead z plikiem",
                "email": "lead@example.com",
                "phone": "123456789",
                "company": "Example Company",
                "inquiry_type": QuoteRequest.InquiryType.B2B_COMPONENTS,
                "scale": QuoteRequest.Scale.SMALL_SERIES,
                "message": "W zalaczniku jest rysunek elementu do wyceny.",
                "consent": "on",
                "attachments": uploaded_file,
            },
        )

        self.assertEqual(response.status_code, 302)
        quote = QuoteRequest.objects.get(name="Lead z plikiem")
        self.assertEqual(quote.attachments.count(), 1)
        self.assertEqual(len(mail.outbox), 2)
        self.assertEqual(len(mail.outbox[0].attachments), 1)
        attachment = mail.outbox[0].attachments[0]
        self.assertEqual(attachment.filename, "rysunek-testowy.txt")
        self.assertEqual(attachment.content, "testowy opis rysunku")
        self.assertEqual(attachment.mimetype, "text/plain")
        self.assertEqual(mail.outbox[1].attachments, [])

    def test_company_notification_skips_missing_attachment_file(self):
        quote = QuoteRequest.objects.create(
            name="Lead z brakujacym plikiem",
            email="lead@example.com",
            phone="123456789",
            inquiry_type=QuoteRequest.InquiryType.B2B_COMPONENTS,
            message="Prosze o wycene elementu.",
            consent=True,
        )
        QuoteAttachment.objects.create(
            quote_request=quote,
            file="quote-attachments/missing/missing.pdf",
            original_name="missing.pdf",
        )

        with self.assertLogs("leads.email", level="ERROR"):
            send_quote_emails(quote)

        self.assertEqual(len(mail.outbox), 2)
        self.assertEqual(mail.outbox[0].attachments, [])
        self.assertEqual(mail.outbox[1].attachments, [])

    def test_prod_smoke_quote_is_saved_labeled_and_does_not_send_email(self):
        response = self.client.post(
            f"{reverse('quote')}?piecode_dev=1&kajax_smoke=1",
            {
                "name": "Lead E2E",
                "phone": "604000000",
                "company": "E2E Manufacturing",
                "inquiry_type": QuoteRequest.InquiryType.CUSTOM_ARTISTIC,
                "scale": QuoteRequest.Scale.SMALL_SERIES,
                "location": "Gdansk / Europa",
                "expected_timing": "Probka w czerwcu",
                "message": "Potrzebujemy krotkiej serii precyzyjnych elementow drewnianych wedlug rysunku.",
                "consent": "on",
            },
        )

        self.assertEqual(response.status_code, 302)
        quote = QuoteRequest.objects.get(name="Lead E2E", phone="604000000")
        self.assertIn(SMOKE_ADMIN_NOTE_PREFIX, quote.admin_notes)
        self.assertEqual(len(mail.outbox), 0)
        self.assertEqual(list(smoke_cleanup_queryset()), [quote])

    @override_settings(
        PIECODE_LEAD_SYNC_ENABLED=True,
        PIECODE_LEAD_SYNC_SEND_LEAD=True,
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
        self.assertEqual(event_payload["event_name"], "generate_lead")
        self.assertEqual(event_payload["event_id"], f"kajax-quote-{quote.pk}-generate-lead")
        self.assertEqual(event_payload["params"]["gclid"], "test-click-id")
        self.assertEqual(event_payload["params"]["business_line"], "b2b_wooden_components")
        self.assertEqual(event_payload["params"]["service_area"], "poland_wide")
        self.assertEqual(lead_payload["workspace_id"], "kajax")
        self.assertEqual(lead_payload["gclid"], "test-click-id")
        self.assertEqual(lead_payload["last_utm_campaign"], "kajax_test")

    @override_settings(
        PIECODE_LEAD_SYNC_ENABLED=True,
        PIECODE_LEAD_SYNC_SEND_LEAD=False,
        PIECODE_LEAD_SYNC_LEAD_URL="https://piecode.example/api/leads",
        PIECODE_LEAD_SYNC_EVENT_URL="https://piecode.example/api/events",
    )
    @patch("leads.piecode_sync.post_json")
    def test_quote_form_syncs_only_non_pii_event_by_default(self, post_json):
        post_json.return_value = {"ok": True, "accepted": 1}

        response = self.client.post(
            f"{reverse('quote')}?utm_source=google&utm_medium=cpc&utm_campaign=kajax_test&gclid=test-click-id",
            {
                "name": "Event Only Lead",
                "email": "lead@example.com",
                "phone": "123456789",
                "inquiry_type": QuoteRequest.InquiryType.CONSTRUCTION_JOINERY,
                "message": "Proszę o wycenę schodów drewnianych.",
                "consent": "on",
            },
        )

        self.assertEqual(response.status_code, 302)
        quote = QuoteRequest.objects.get(name="Event Only Lead")
        self.assertEqual(quote.central_sync_status, "event_only")
        self.assertEqual(quote.central_lead_id, "")
        self.assertEqual(post_json.call_count, 1)

        event_url, event_payload = post_json.call_args.args
        self.assertEqual(event_url, "https://piecode.example/api/events")
        self.assertEqual(event_payload["workspace_id"], "kajax")
        self.assertEqual(event_payload["event_name"], "generate_lead")
        self.assertEqual(event_payload["event_id"], f"kajax-quote-{quote.pk}-generate-lead")
        self.assertEqual(event_payload["params"]["business_line"], "construction_joinery")
        self.assertEqual(event_payload["params"]["service_area"], "pomerania")
        self.assertNotIn("email", event_payload["params"])
        self.assertNotIn("phone", event_payload["params"])
        self.assertNotIn("message", event_payload["params"])
