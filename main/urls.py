from django.conf.urls import url

from . import views, viewPdf, html2pdf, viewPdf2
from viewPdf2 import hello_pdf_5, hello_pdf_6

urlpatterns = [
    # ex: / 
    url(r'^$', views.index, name='index'),
    # ex: /5/
    url(r'^(?P<_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /5/results/
    url(r'^results/(?P<qid>[0-9]+)/$', views.results, name='results'),
    # ex: 5/vote/
    url(r'^vote/(?P<id>[0-9]+)/$', views.vote, name='vote'),

    url(r'^report/pdf$', viewPdf.generatePdf, name='getPdf'),

    url(r'^report/pdf/bytes$', viewPdf.generatePdfBytes, name='getPdfBytes'),

    url(r'^report/html2pdf$', html2pdf.convert, name='html2pdf'),

    url(r"^hello/pdf$", viewPdf2.HelloPDFView.as_view(), name='getPdf2'),

    url(r"^hello/pdf2$", viewPdf2.HelloPDFView2.as_view(), name='getPdf3'),

    url(r"^hello/pdf3$", viewPdf2.HelloPDFView3.as_view(), name='getPdf4'),

    url(r"^hello/pdf4$", viewPdf2.HelloPDFView4.as_view(), name='getPdf5'),

    url(r"^hello/pdf5$", hello_pdf_5, name='getPdf6'),

    url(r"^hello/pdf6$", hello_pdf_6, name='getPdf7'),
]