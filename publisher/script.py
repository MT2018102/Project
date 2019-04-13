
# coding: utf-8

# In[33]:


import os
import math
from .PyPDF3 import PdfFileReader, PdfFileWriter
from django.conf import settings
def pdf_splitter(path,start_page,end_page,chapter_name,book_name):
    print('path: ',path,'no: ',type(start_page))
    fname = os.path.splitext(os.path.basename(path))[0]
    pdf = PdfFileReader(path)
    print(pdf.getNumPages())
    i=0
    print(type(start_page))
    print(type(end_page))
    start_page=int(start_page)
    end_page=int(end_page)
    pdf_writer = PdfFileWriter()
    for k in range(start_page-1,end_page):
        pdf_writer.addPage(pdf.getPage(k))
    chapter_name=book_name.replace(".pdf", "_")+chapter_name+'.pdf'
    path=settings.MEDIA_ROOT+'\\'+chapter_name
    with open(path, 'wb') as out:
        pdf_writer.write(out)
    print('Created: {}'.format(chapter_name))
    return chapter_name,path
