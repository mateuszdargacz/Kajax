from django.db import models
from django.utils.translation import gettext_lazy as _


class QuoteRequest(models.Model):
    class InquiryType(models.TextChoices):
        B2B_COMPONENTS = "b2b_components", _("Elementy drewniane B2B")
        CONSTRUCTION_JOINERY = "construction_joinery", _("Stolarka budowlana")
        CUSTOM_ARTISTIC = "custom_artistic", _("Custom / stolarstwo artystyczne")
        OTHER = "other", _("Inne")

    class Scale(models.TextChoices):
        ONE_PIECE = "one_piece", _("1 sztuka")
        SMALL_SERIES = "small_series", _("Mała seria")
        RECURRING = "recurring", _("Stała współpraca")
        UNKNOWN = "unknown", _("Nie wiem jeszcze")

    name = models.CharField(_("imię i nazwisko"), max_length=160)
    email = models.EmailField(_("email"), blank=True)
    phone = models.CharField(_("telefon"), max_length=64, blank=True)
    company = models.CharField(_("firma"), max_length=180, blank=True)
    inquiry_type = models.CharField(_("typ zapytania"), max_length=64, choices=InquiryType.choices)
    scale = models.CharField(_("skala"), max_length=64, choices=Scale.choices, blank=True, default=Scale.UNKNOWN)
    location = models.CharField(_("lokalizacja"), max_length=180, blank=True)
    expected_timing = models.CharField(_("oczekiwany termin"), max_length=180, blank=True)
    message = models.TextField(_("opis projektu"))
    consent = models.BooleanField(_("zgoda kontaktowa"), default=False)
    language = models.CharField(_("język"), max_length=16, blank=True)
    source_path = models.CharField(_("źródłowy URL"), max_length=255, blank=True)
    user_agent = models.TextField(_("user agent"), blank=True)
    central_lead_id = models.CharField(_("centralny ID leada"), max_length=80, blank=True)
    central_sync_status = models.CharField(_("status synchronizacji centralnej"), max_length=40, blank=True)
    central_sync_last_error = models.TextField(_("ostatni błąd synchronizacji centralnej"), blank=True)
    central_synced_at = models.DateTimeField(_("zsynchronizowano centralnie"), null=True, blank=True)
    is_handled = models.BooleanField(_("obsłużone"), default=False)
    admin_notes = models.TextField(_("notatki"), blank=True)
    created_at = models.DateTimeField(_("utworzono"), auto_now_add=True)
    updated_at = models.DateTimeField(_("zaktualizowano"), auto_now=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = _("zapytanie ofertowe")
        verbose_name_plural = _("zapytania ofertowe")

    def __str__(self):
        return f"{self.name} - {self.get_inquiry_type_display()}"


def quote_attachment_path(instance, filename):
    return f"quote-attachments/{instance.quote_request_id}/{filename}"


class QuoteAttachment(models.Model):
    quote_request = models.ForeignKey(
        QuoteRequest,
        on_delete=models.CASCADE,
        related_name="attachments",
        verbose_name=_("zapytanie"),
    )
    file = models.FileField(_("plik"), upload_to=quote_attachment_path)
    original_name = models.CharField(_("oryginalna nazwa"), max_length=255)
    uploaded_at = models.DateTimeField(_("dodano"), auto_now_add=True)

    class Meta:
        verbose_name = _("załącznik zapytania")
        verbose_name_plural = _("załączniki zapytań")

    def __str__(self):
        return self.original_name
