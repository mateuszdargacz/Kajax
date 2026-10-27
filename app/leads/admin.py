from django.contrib import admin
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.urls import path, reverse
from django.utils.html import format_html

from leads.attachments import attachment_response
from leads.models import QuoteAttachment, QuoteRequest


class QuoteAttachmentInline(admin.TabularInline):
    model = QuoteAttachment
    extra = 0
    readonly_fields = ["original_name", "uploaded_at", "download"]
    fields = ["original_name", "download", "uploaded_at"]

    @admin.display(description="Pobierz plik")
    def download(self, obj):
        if not obj.pk or not obj.file:
            return "-"
        return format_html('<a href="{}">{}</a>', reverse(
            "admin:leads_quoteattachment_download", args=[obj.quote_request_id, obj.pk]),
            obj.original_name or "Pobierz")


@admin.register(QuoteRequest)
class QuoteRequestAdmin(admin.ModelAdmin):
    list_display = [
        "created_at",
        "name",
        "company",
        "inquiry_type",
        "scale",
        "email",
        "phone",
        "central_sync_status",
        "is_handled",
    ]
    list_filter = ["inquiry_type", "scale", "central_sync_status", "is_handled", "created_at"]
    search_fields = ["name", "email", "phone", "company", "message"]
    readonly_fields = [
        "created_at",
        "updated_at",
        "language",
        "source_path",
        "user_agent",
        "central_lead_id",
        "central_sync_status",
        "central_sync_last_error",
        "central_synced_at",
    ]
    inlines = [QuoteAttachmentInline]

    def get_urls(self):
        return [path(
            "<int:quote_id>/attachments/<int:attachment_id>/download/",
            self.admin_site.admin_view(self.download_attachment),
            name="leads_quoteattachment_download",
        )] + super().get_urls()

    def download_attachment(self, request, quote_id, attachment_id):
        attachment = get_object_or_404(QuoteAttachment.objects.select_related("quote_request"),
            pk=attachment_id, quote_request_id=quote_id)
        if not self.has_view_or_change_permission(request, attachment.quote_request):
            raise Http404
        return attachment_response(attachment)
