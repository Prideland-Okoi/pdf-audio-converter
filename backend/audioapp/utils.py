import os
import PyPDF2
from io import BytesIO

def extract_text(filename):
    reader = open(filename, 'rb')
    pdfRead = PyPDF2.PdfReader(io.BytesIO(reader))
    num = len(pdfRead.pages)
    page_num = range(num)
    for x in page_num:
        paige = pdfRead.pages[x]
        mytext = paige.extract_text()
        reader.close()
        return mytext
