from django import forms

from leads.copy import get_form_copy
from leads.models import QuoteRequest


class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True


class MultipleFileField(forms.FileField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleFileInput())
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            return [single_file_clean(item, initial) for item in data]
        if data:
            return [single_file_clean(data, initial)]
        return []


class QuoteRequestForm(forms.ModelForm):
    primary_fields = ["name", "phone", "email", "inquiry_type", "message", "consent"]
    optional_fields = ["company", "scale", "location", "expected_timing", "attachments"]

    attachments = MultipleFileField(
        required=False,
    )
    consent = forms.BooleanField(
        required=True,
    )

    class Meta:
        model = QuoteRequest
        fields = [
            "name",
            "email",
            "phone",
            "company",
            "inquiry_type",
            "scale",
            "location",
            "expected_timing",
            "message",
            "consent",
        ]
        widgets = {
            "message": forms.Textarea(attrs={"rows": 6}),
        }

    def __init__(self, *args, **kwargs):
        language_code = kwargs.pop("language_code", "pl")
        super().__init__(*args, **kwargs)
        copy = get_form_copy(language_code)

        self.fields["email"].required = False
        self.fields["phone"].required = False
        self.fields["scale"].required = False
        self.fields["scale"].initial = QuoteRequest.Scale.UNKNOWN
        self.fields["attachments"].label = copy["attachments"]
        self.fields["attachments"].help_text = copy["attachments_help"]
        self.fields["consent"].label = copy["consent"]

        self.fields["inquiry_type"].choices = [
            (QuoteRequest.InquiryType.B2B_COMPONENTS, copy["b2b_components"]),
            (QuoteRequest.InquiryType.CONSTRUCTION_JOINERY, copy["construction_joinery"]),
            (QuoteRequest.InquiryType.CUSTOM_ARTISTIC, copy["custom_artistic"]),
            (QuoteRequest.InquiryType.OTHER, copy["other"]),
        ]
        self.fields["scale"].choices = [
            (QuoteRequest.Scale.UNKNOWN, copy["unknown"]),
            (QuoteRequest.Scale.ONE_PIECE, copy["one_piece"]),
            (QuoteRequest.Scale.SMALL_SERIES, copy["small_series"]),
            (QuoteRequest.Scale.RECURRING, copy["recurring"]),
        ]

        for name, label in {
            "name": copy["name"],
            "email": copy["email"],
            "phone": copy["phone"],
            "company": copy["company"],
            "inquiry_type": copy["inquiry_type"],
            "scale": copy["scale"],
            "location": copy["location"],
            "expected_timing": copy["expected_timing"],
            "message": copy["message"],
        }.items():
            self.fields[name].label = label

        self.fields["company"].help_text = copy["company_help"]
        self.fields["location"].help_text = copy["location_help"]
        self.fields["expected_timing"].help_text = copy["expected_timing_help"]
        self.fields["message"].help_text = copy["message_help"]
        self.contact_required_message = copy["contact_required"]

        for field in self.fields.values():
            css_class = "form-control"
            if isinstance(field.widget, forms.CheckboxInput):
                css_class = "form-check-input"
            field.widget.attrs["class"] = css_class

    def clean(self):
        cleaned_data = super().clean()
        if not cleaned_data.get("phone") and not cleaned_data.get("email"):
            raise forms.ValidationError(self.contact_required_message)
        return cleaned_data

    def clean_scale(self):
        return self.cleaned_data.get("scale") or QuoteRequest.Scale.UNKNOWN

    def primary_bound_fields(self):
        return [self[name] for name in self.primary_fields]

    def optional_bound_fields(self):
        return [self[name] for name in self.optional_fields]

    def has_optional_errors(self):
        return any(self.errors.get(name) for name in self.optional_fields)
