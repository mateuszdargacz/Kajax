from django.core import mail
from django.test import TestCase, override_settings
from django.urls import reverse

from leads.models import QuoteRequest


@override_settings(EMAIL_BACKEND="django.core.mail.backends.locmem.EmailBackend")
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

        quote = QuoteRequest.objects.get()
        self.assertEqual(quote.email, "lead@example.com")
        self.assertEqual(quote.inquiry_type, QuoteRequest.InquiryType.B2B_COMPONENTS)

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

        quote = QuoteRequest.objects.get()
        self.assertEqual(quote.email, "")
        self.assertEqual(quote.phone, "123456789")
        self.assertEqual(quote.scale, QuoteRequest.Scale.UNKNOWN)
