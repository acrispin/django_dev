from django.conf.urls import url
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    # ex: /polls/
    url(r'^$', views.index, name='index'),
    # ex: /polls/5/
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /polls/5/results/
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /polls/5/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
    # ex: /polls/home/
    url(r'^home$', views.homepage, name='home'),
    # /polls/report/line
    url(r'^report/line', TemplateView.as_view(template_name='polls/line.html'), name='line'),
    # /polls/report/column
    url(r'^report/column', TemplateView.as_view(template_name='report/column.html'), name='column'),
    # /polls/report/pie
    url(r'^report/pie', TemplateView.as_view(template_name='pie.html'), name='pie'),
]