from django.conf.urls import patterns, url
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns
from apprest.viewsets import LibroViewSet, AutorViewSet, FileViewSet
from apprest.viewapi import RestApiView, RestApiViewJson
from apprest.viewbase import FileList, FileDetail

"""
{% url 'rest:libro-list' %} --> http://localhost:8001/api/rest/libros/
{% url 'rest:autor-list' %} --> http://localhost:8001/api/rest/autores/
{% url 'rest:file-list' %} --> http://localhost:8001/api/rest/files/
"""
router = DefaultRouter()
router.register(r'libros', LibroViewSet, base_name='libro')
router.register(r'autores', AutorViewSet, base_name='autor')
router.register(r'files', FileViewSet, base_name='file')


""" 
{% url 'rest2:my_rest_view_1' 2 %} --> http://localhost:8001/api/rest/v1.0/resource/2
{% url 'rest2:my_rest_view_1' 3 %}?format=json&arg1=128&arg2=hola" --> http://localhost:8001/api/rest/v1.0/resource/3?format=json&arg1=128&arg2=hola
{% url 'rest2:my_rest_view_1' 70 %}/?format=json&arg1=128&arg2=hola --> http://localhost:8001/api/rest/v1.0/resource/70/?format=json&arg1=128&arg2=hola
{% url 'rest2:my_rest_view_2' %} --> http://localhost:8001/api/rest/v1.0/resource
{% url 'rest2:my_rest_view_2' %}?code=00198&active=true --> http://localhost:8001/api/rest/v1.0/resource?code=00198&active=true
"""
urls2 = patterns('',
    # this URL passes resource_id in **kw to RestApiView
    url(r'^v1.0/resource/(?P<resource_id>\d+)[/]?$', RestApiView.as_view(), name='my_rest_view_1'),
    url(r'^v1.0/resource[/]?$', RestApiView.as_view(), name='my_rest_view_2'),
)


"""
tag url templates : 
{% url 'rest3:my_json_1' n1=5 %} --> http://localhost:8001/api/rest/5/json/
{% url 'rest3:my_json_2' n1=5 n2=2 %} --> http://localhost:8001/api/rest/5/json/2/
{% url 'rest3:my_json_3' n1=5 n2=2 %} --> http://localhost:8001/api/rest/5/json2/
{% url 'rest3:my_json_4' p1=1 p2=2 p3=3 %} --> http://localhost:8001/api/rest/1/2/3/
{% url 'rest3:my_json_5' m1=1091 m2=2245 m3=09 %} --> http://localhost:8001/api/rest/multiple/params/1091/2245/9/
{% url 'rest3:my_json_5' 1091 2245 09 %} -- > http://localhost:8001/api/rest/multiple/params/1091/2245/9/
"""
urls3 = patterns('',
    url(r'^(?P<n1>\d)/json/', RestApiViewJson.as_view(), name='my_json_1'),
    url(r'^(?P<n1>\d)/json/(?P<n2>\d)/', RestApiViewJson.as_view(), name='my_json_2'), # en el **kw solo obtiene el n1
    url(r'^(?P<n1>\d)/json(?P<n2>\d)/', RestApiViewJson.as_view(), name='my_json_3'), # en el **kw obtiene n1 y n2
    url(r'^(?P<p1>\d)/(?P<p2>\d)/(?P<p3>\d)/', RestApiViewJson.as_view(), name='my_json_4'), # en el **kw obtiene p1, p2 y p3
    url(r'^multiple/params/(?P<m1>\d+)/(?P<m2>\d+)/(?P<m3>\d+)/', RestApiViewJson.as_view(), name='my_json_5'), # con mas de un digito
)


"""
{% url 'rest4:base_file' %} --> http://localhost:8001/api/rest/base/files/
{% url 'rest4:base_file_pk' 2 %} --> http://localhost:8001/api/rest/base/files/2/
"""
urls4 = [
    url(r'^base/files/$', FileList.as_view(), name='base_file'),
    url(r'^base/files/(?P<pk>[0-9]+)/$', FileDetail.as_view(), name='base_file_pk'),
]

#urls4 = format_suffix_patterns(urls4) ## ??????????????


"""
fuentes
http://www.django-rest-framework.org/tutorial/6-viewsets-and-routers/

nombre de los routers
http://www.django-rest-framework.org/api-guide/routers/

........................................................................................
base_name - The base to use for the URL names that are created. If unset the basename will be automatically generated based on the queryset attribute of the viewset, if it has one. Note that if the viewset does not include a queryset attribute then you must set base_name when registering the viewset.

URL pattern: ^users/$ Name: 'user-list'
URL pattern: ^users/{pk}/$ Name: 'user-detail'
URL pattern: ^accounts/$ Name: 'account-list'
URL pattern: ^accounts/{pk}/$ Name: 'account-detail'

The base_name argument is used to specify the initial part of the view name pattern. In the example above, that's the user or account part.
........................................................................................

con esto en el html se puede usar estas rutas con su nombre, ejm:
<li><a href="{% url 'rest:libro-list' %}">Libros</a></li>
<li><a href="{% url 'rest:autor-list' %}">Autor</a></li>
"""