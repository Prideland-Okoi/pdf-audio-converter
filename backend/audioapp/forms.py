from django.core.validators import FileExtensionValidator
from django import forms
from django.forms import ModelForm
from .models import TextAudio, UploadPDF

class TextAudioForm(ModelForm):
    class Meta:
        model = TextAudio
        exclude =['date_created']

        widgets = {
            'language' : forms.Select()
        }

class UploadPDFForm(ModelForm):
    class Meta:
        model = UploadPDF
        exclude = ['date_created']
        validators = [FileExtensionValidator(allowed_extensions = ['pdf'])]

        widgets = {
                'language': forms.Select()
                }
        def validate_file_extension(pdf):
            if not pdf.name.endswith('.pdf'):
                raise forms.ValidationError("Only PDF file is accepted")
