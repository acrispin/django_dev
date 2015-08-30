from django.conf.urls import url

from . import views, viewPdf, html2pdf

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
]