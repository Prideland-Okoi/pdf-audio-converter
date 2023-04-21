from django.db import models
import datetime

# Create your models here.
language_choice = (
        ('en-us', 'English-United States'),
        ('af', 'Afrikaans'),
        ('sq', 'Albanian'),
        ('ar', 'Arabic'),
        ('hy', 'Armenian'),
        ('bn', 'Bengali'),
        ('ca', 'Catalan'),
        ('zh', 'Chinese'),
        ('zh-cn', 'Chinese-zh'),
        ('zh-tw', 'Taiwan'),
        ('zh-yue', 'Cantonese'),
        ('hr', 'Croatian'),
        ('cs', 'Czech'),
        ('da', 'Danish'),
        ('nl', 'Dutch'),
        ('en', 'English'),
        ('en-au', 'English-Australia'),
        ('en-uk', 'English-United Kingdom'),
        ('eo', 'Esperanto'),
        ('fi', 'Finnish'),
        ('fr', 'French'),
        ('de', 'German'),
        ('hu', 'Hungarian'),
        ('el', 'Greek'),
        ('hi', 'Hindi'),
        ('is', 'Icelandic'),
        ('id', 'Indonesian'),
        ('it', 'Italian'),
        ('ja', 'Japanese'),
        ('km', 'Cambodian'),
        ('ko', 'Korean'),
        ('la', 'Latin'),
        ('lv', 'Latvian'),
        ('mk', 'Macedonian'),
        ('no', 'Norwegian'),
        ('pl', 'Polish'),
        ('pt','Portuguese'),
        ('ro', 'Romanian'),
        ('ru', 'Russian'),
        ('sr','Serbian'),
        ('si', 'Sinhala'),
        ('sk','Slovak'),
        ('es', 'Spanish'),
        ('es-es', 'Spanish-Spain'),
        ('es-us', 'Spanish-USA'),
        ('sw', 'Swahili'),
        ('sv', 'Swedish'),
        ('ta',  'Tamil'),
        ('th', 'Thai'),
        ('tr', 'Turkish'),
        ('uk', 'Ukrainian'),
        ('vi', 'Vietnamese'),
        ('cy', 'Welsh'),
    )

class TextAudio(models.Model):
    text_name = models.CharField(max_length=20)
    info = models.TextField()
    lang= models.CharField(max_length=10, choices=language_choice, default='English - United States')
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{} - {}".format(self.text_name, self.date_created)

class UploadPDF(models.Model):
    pdf_name = models.CharField(max_length=30)
    pdf = models.FileField(upload_to='pdffolder', blank=True, null=True)
    lang = models.CharField(max_length=10, choices=language_choice, default='English - United States')
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{} - {}".format(self.pdf_name, self.date_created)

class PDFAudio(models.Model):
    pdf_name = models.CharField(max_length=20)
    mytext = models.TextField(null=True)
    lang= models.CharField(max_length=10)
    date_created = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return "{} - {}".format(self.pdf_name, self.date_created)
