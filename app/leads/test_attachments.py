import tempfile
from unittest.mock import patch

from django.contrib.auth.models import Permission, User
from django.core import mail
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase, override_settings
from django.urls import reverse

from leads.attachments import attachment_grant
from leads.email import _send_company_notification, notification_attachment_batches
from leads.models import QuoteAttachment, QuoteRequest
from leads.piecode_sync import attachment_items


@override_settings(EMAIL_BACKEND="django.core.mail.backends.locmem.EmailBackend", LEAD_EMAIL_FAIL_SILENTLY=False)
class AttachmentAccessTests(TestCase):
    def setUp(self):
        directory = tempfile.TemporaryDirectory()
        self.addCleanup(directory.cleanup)
        setting = override_settings(MEDIA_ROOT=directory.name)
        setting.enable()
        self.addCleanup(setting.disable)
        self.quote = QuoteRequest.objects.create(name="Synthetic lead", email="fixture@example.com",
            inquiry_type="other", message="Synthetic attachment test", central_lead_id="a" * 24)
        self.attachment = QuoteAttachment.objects.create(quote_request=self.quote,
            original_name="budget.xlsx", file=SimpleUploadedFile("budget.xlsx", b"synthetic-xlsx"))
        self.url = reverse("piecode-attachment", args=[self.attachment.pk])
        self.grant = attachment_grant(self.attachment)

    def test_source_download_requires_exact_grant_and_keeps_it_out_of_urls(self):
        self.assertEqual(self.client.get(self.url).status_code, 404)
        self.assertEqual(self.client.get(self.url, HTTP_X_PIECODE_ATTACHMENT_GRANT=self.grant + "x").status_code, 404)
        response = self.client.get(self.url, HTTP_X_PIECODE_ATTACHMENT_GRANT=self.grant)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(b"".join(response.streaming_content), b"synthetic-xlsx")
        self.assertEqual(response["X-Piecode-Lead-ID"], "a" * 24)
        self.assertEqual(response["Cache-Control"], "private, no-store")
        self.assertIn('attachment;', response["Content-Disposition"])
        self.assertNotIn(self.grant, self.url)

    def test_wrong_attachment_deleted_or_replaced_file_cannot_use_grant(self):
        other = QuoteAttachment.objects.create(quote_request=self.quote, original_name="other.txt",
            file=SimpleUploadedFile("other.txt", b"other"))
        self.assertEqual(self.client.get(reverse("piecode-attachment", args=[other.pk]),
            HTTP_X_PIECODE_ATTACHMENT_GRANT=self.grant).status_code, 404)
        self.attachment.file = "quote-attachments/replaced.xlsx"
        self.attachment.save(update_fields=["file"])
        self.assertEqual(self.client.get(self.url, HTTP_X_PIECODE_ATTACHMENT_GRANT=self.grant).status_code, 404)

    def test_admin_download_requires_staff_and_model_permission(self):
        url = reverse("admin:leads_quoteattachment_download", args=[self.quote.pk, self.attachment.pk])
        self.assertEqual(self.client.get(url).status_code, 302)
        user = User.objects.create_user(username="fixture", is_staff=True)
        self.client.force_login(user)
        self.assertEqual(self.client.get(url).status_code, 404)
        user.user_permissions.add(Permission.objects.get(codename="view_quoterequest"))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(b"".join(response.streaming_content), b"synthetic-xlsx")

    def test_sync_metadata_contains_bound_reference_not_public_media_url(self):
        item = attachment_items(self.quote)[0]
        self.assertEqual(item["source_quote_id"], str(self.quote.pk))
        self.assertEqual(item["source_attachment_id"], str(self.attachment.pk))
        self.assertEqual(item["size"], 14)
        self.assertEqual(item["source_grant"], self.grant)
        self.assertNotIn("url", item)

    def test_mail_batches_include_every_file_once_and_only_notify_company(self):
        files = [(f"fixture-{index}.jpg", b"image", "image/jpeg") for index in range(5)]
        batches = notification_attachment_batches(files, max_bytes=11)
        self.assertEqual([len(batch) for batch in batches], [2, 2, 1])
        self.assertEqual([item for batch in batches for item in batch], files)
        with patch("leads.email.notification_attachment_batches", return_value=batches):
            _send_company_notification(self.quote, ["operator@example.com"])
        self.assertEqual(len(mail.outbox), 3)
        self.assertEqual([len(message.attachments) for message in mail.outbox], [2, 2, 1])
        self.assertTrue(mail.outbox[0].subject.endswith("[1/3]"))
        for message in mail.outbox:
            self.assertEqual(message.to, ["operator@example.com"])
            self.assertIn(f"/quoterequest/{self.quote.pk}/change/", message.body)
            self.assertNotIn(self.grant, message.body)
