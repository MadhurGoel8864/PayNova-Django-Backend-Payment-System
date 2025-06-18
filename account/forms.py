from django import forms 
from account.models import KYC
from django.forms import ImageField, FileInput, DateInput

class DateInput(forms.DateInput):
    input_type = 'date'

class KYCForm(forms.ModelForm):
    identity_image = ImageField(widget=FileInput, required=True)
    image = ImageField(widget=FileInput, required=True)
    signature = ImageField(widget=FileInput, required=True)

    class Meta:
        model = KYC
        fields = [ 'full_name', 'image', 'marrital_status', 'gender', 'identity_type', 'identity_image', 'date_of_birth', 'signature', 'country', 'state', 'city', 'mobile', 'fax']
        widgets = {
            "full_name": forms.TextInput(attrs={"placeholder":"Full Name", "required": True}),
            "mobile": forms.TextInput(attrs={"placeholder":"Mobile Number", "required": True}),
            "fax": forms.TextInput(attrs={"placeholder":"Fax Number", "required": True}),
            "country": forms.TextInput(attrs={"placeholder":"Country", "required": True}),
            "state": forms.TextInput(attrs={"placeholder":"State", "required": True}),
            "city": forms.TextInput(attrs={"placeholder":"City", "required": True}),
            'date_of_birth': DateInput(attrs={"required": True}),
            'gender': forms.Select(attrs={"required": True}),
            'marrital_status': forms.Select(attrs={"required": True}),
            'identity_type': forms.Select(attrs={"required": True}),
        }

class EditKYCForm(KYCForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Disable all fields by default
        self.disable_all_fields()
    
    def disable_all_fields(self):
        """Disable all form fields"""
        for field_name, field in self.fields.items():
            if hasattr(field.widget, 'attrs'):
                field.widget.attrs['disabled'] = 'disabled'
                field.widget.attrs['readonly'] = 'readonly'
    
    def enable_all_fields(self):
        """Enable all form fields"""
        for field_name, field in self.fields.items():
            if hasattr(field.widget, 'attrs'):
                if 'disabled' in field.widget.attrs:
                    del field.widget.attrs['disabled']
                if 'readonly' in field.widget.attrs:
                    del field.widget.attrs['readonly']
    
    def clean(self):
        """Remove disabled attribute before validation to allow form submission"""
        cleaned_data = super().clean()
        # Remove disabled attributes so the form can be submitted
        for field_name, field in self.fields.items():
            if hasattr(field.widget, 'attrs'):
                if 'disabled' in field.widget.attrs:
                    del field.widget.attrs['disabled']
                if 'readonly' in field.widget.attrs:
                    del field.widget.attrs['readonly']
        return cleaned_data