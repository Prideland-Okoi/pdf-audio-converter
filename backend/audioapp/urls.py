from django.urls import path
from .import views

app_name = 'audioapp'

urlpatterns = [
    path("", views.home, name = 'home'),
    path('audio-create', views.audio_create, name = 'audio-create'),
    path('audio-details', views.audio_details, name ='audio-details'),
    path('audio-modify/<int:id>', views.audio_modify, name = 'audio-modify'),
    path('audio-delete/<int:id>', views.audio_delete, name ='audio-delete'),
    path('pdf-create', views.pdf_create, name = 'pdf-create'),
    path('pdf-details', views.pdf_details, name ='pdf-details'),
    path('pdfaudio-modify/<int:id>', views.pdfaudio_modify, name = 'pdfaudio-modify'),
    path('pdf-delete/<int:id>', views.pdf_delete, name ='pdf-delete'),
]
