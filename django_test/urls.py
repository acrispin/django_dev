from django.conf.urls import patterns, include, url
from django.contrib import admin
from apprest.urls import router
from django.conf import settings

admin.autodiscover()
 
urlpatterns = patterns('',    
    url(r'^', include('main.urls', namespace="main")),
    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^rest/api/', include(router.urls, namespace="rest")),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')), 
    url(r'^admin/', include(admin.site.urls)),
)
