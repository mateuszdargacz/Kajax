from django.contrib import admin

from leads.models import QuoteAttachment, QuoteRequest


class QuoteAttachmentInline(admin.TabularInline):
    model = QuoteAttachment
    extra = 0
    readonly_fields = ["original_name", "uploaded_at"]


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
        "is_handled",
    ]
    list_filter = ["inquiry_type", "scale", "is_handled", "created_at"]
    search_fields = ["name", "email", "phone", "company", "message"]
    readonly_fields = ["created_at", "updated_at", "language", "source_path", "user_agent"]
    inlines = [QuoteAttachmentInline]
