from django.contrib import admin
from .models import TextAudio, PDFAudio, UploadPDF

# Register your models here.
admin.site.register(TextAudio)
admin.site.register(PDFAudio)
admin.site.register(UploadPDF)
