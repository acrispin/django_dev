from django.conf.urls import patterns, include, url
from django.contrib import admin
from apprest.urls import router, urls2, urls3, urls4
from django.conf import settings

admin.autodiscover()
 
urlpatterns = patterns('',    
    url(r'^', include('main.urls', namespace="main")),
    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^api/rest/', include(router.urls, namespace="rest")),
    url(r'^api/rest/', include(urls2, namespace="rest2")),
    url(r'^api/rest/', include(urls3, namespace="rest3")),
    url(r'^api/rest/', include(urls4, namespace="rest4")),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')), 
    url(r'^admin/', include(admin.site.urls)),
)
