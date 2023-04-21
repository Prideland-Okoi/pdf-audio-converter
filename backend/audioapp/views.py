import os
import io
from django.conf import settings
from django.templatetags.static import static
import PyPDF2

from django.shortcuts import render, redirect
from gTTS.templatetags.gTTS import say
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import TextAudio,UploadPDF, PDFAudio
from .forms import TextAudioForm, UploadPDFForm

from .utils import extract_text

# Create your views here.

def home(request):
    context = {}
    context['pdf_audio'] = PDFAudio.objects.order_by('date_created')[:1]
    context['text_audio'] = TextAudio.objects.order_by('date_created')[:1]
    #context['text_audio'] = TextAudio.objects.filter(name='date_created').last()
    #context['text_audio'] = list(TextAudio.objects.all())[-1]
    return render(request, 'audioapp/index.html', context)

def pdf_create(request):
    if request.method == 'POST':
        pdf_form = UploadPDFForm(request.POST, request.FILES)
        if pdf_form.is_valid():
            filename = request.POST.get('pdf_name')
            lang = request.POST.get('lang')
            pdf = request.FILES['pdf'].read()
            if pdf:
                pdfRead = PyPDF2.PdfReader(io.BytesIO(pdf))
                num = len(pdfRead.pages)
                page_num = range(num)
                mytext = ""
                for x in page_num:
                    paige = pdfRead.pages[x]
                    text = paige.extract_text()
                    mytext += text
                #pdfRead.close()
                create_file = PDFAudio.objects.create(pdf_name = filename, lang = lang, mytext = mytext)
            #pdf_form.save()
            return redirect('audioapp:pdf-details')
    else:
        context = {}
        context['pdf_form'] = UploadPDFForm()
    return render(request, 'audioapp/pdf_create.html', context)

def pdf_details(request):
    pdf_audio = PDFAudio.objects.all()
    context = {}
    context['pdf_audio'] = PDFAudio.objects.all()
    return render(request, 'audioapp/pdf_details.html', context)

def pdfaudio_modify(request, id):
    pdf_obj = PDFAudio.objects.get(id=id)
    if request.method == 'GET':
        pdf_form = PDFAudioForm(instance=pdf_obj)
    else:
        pdf_form = PDFAudioForm(request.POST)
        if form.is_valid():
            pdf_form.save()
            return redirect('audioapp:pdf-details')
    return render(request, 'audioapp/pdfaudio_modify.html', {'pdf_form':pdf_form
,})

def pdf_delete(request, id):
    pdf_audio = PDFAudio.objects.filter(id=id).delete()
    #text_audio = TextAudio.objects.get(id=id)
    #text_audio.delete()
    return HttpResponseRedirect(reverse('audioapp:pdf-details'))

def audio_create(request):
    if request.method == 'POST':
        text_form = TextAudioForm(request.POST)
        if text_form.is_valid():
            text_form.save()
            return redirect('audioapp:audio-details')
    else:
        context = {}
        context['text_form'] = TextAudioForm()
    return render(request, 'audioapp/audio_create.html', context)

def audio_details(request):
    text_audio = TextAudio.objects.all()
    context = {}
    context['text_audio'] = TextAudio.objects.all()
    return render(request, 'audioapp/audio_details.html', context)

def audio_modify(request, id):
    text_obj = TextAudio.objects.get(id=id)
    if request.method == 'GET':
        text_form = TextAudioForm(instance=text_obj)
    else:
        text_form = TextAudioForm(request.POST)
        if form.is_valid():
            text_form.save()
            return redirect('audioapp:audio-details')
    return render(request, 'audioapp/audio_modify.html', {'text_form':text_form,})

def audio_delete(request, id):
    text_audio = TextAudio.objects.filter(id=id).delete()
    #text_audio = TextAudio.objects.get(id=id)
    #text_audio.delete()
    return HttpResponseRedirect(reverse('audioapp:audio-details'))
