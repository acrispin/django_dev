from django.conf.urls import patterns, url
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken import views

from apprest.viewsets import LibroViewSet, AutorViewSet, FileViewSet
from apprest.viewapi import RestApiView, RestApiViewJson
from apprest.viewbase import FileList, FileDetail
from apprest.views import home, file_collection, file_element, file_collection2, file_collection3, \
                          file_collection4, file_collection5, file_collection6, file_collection7

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
{% url 'rest5:api_files' %} --> http://localhost:8000/api/rest/api/v1/files/
{% url 'rest5:api_file' 2 %} --> http://localhost:8000/api/rest/api/v1/files/2
"""
urls5 = [
    url(r'^$files/home', home),
    # api
    url(r'^api/v1/files/$', file_collection, name='api_files'),
    url(r'^api/v2/files/$', file_collection2, name='api_files_2'),
    url(r'^api/v3/files/$', file_collection3, name='api_files_3'),
    url(r'^api/v4/files/$', file_collection4, name='api_files_4'),
    url(r'^api/v5/files/$', file_collection5, name='api_files_5'),
    url(r'^api/v6/files/$', file_collection6, name='api_files_6'),
    url(r'^api/v7/files/$', file_collection7, name='api_files_7'),
    url(r'^api/v1/files/(?P<pk>[0-9]+)$', file_element, name='api_file')
]


"""
AUTENTICACION POR TOKEN
http://www.django-rest-framework.org/api-guide/authentication/#tokenauthentication
http://stackoverflow.com/questions/20683824/how-can-i-change-existing-token-in-the-authtoken-of-django-rest-framework
http://stackoverflow.com/questions/14567586/token-authentication-for-restful-api-should-the-token-be-periodically-changed
http://stackoverflow.com/questions/17560228/how-to-use-tokenauthentication-for-api-in-django-rest-framework
http://stackoverflow.com/questions/17507206/how-to-make-a-post-simple-json-using-django-rest-framework-csrf-token-missing-o
https://docs.djangoproject.com/en/1.7/ref/contrib/csrf/#csrf-ajax

## header http para autenticacion por tokens
    Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b

GET
    GET /api/rest/api/v1/files/ HTTP/1.1
    Host: localhost:8000
    Content-Type: application/json
    Authorization: Token 3eb454bbc5a7fea0ca1882a5131eecec602dbb46
    Cache-Control: no-cache

POST
    POST /api/rest/api/v1/files/ HTTP/1.1
    Host: localhost:8000
    Content-Type: application/json
    Authorization: Token 3eb454bbc5a7fea0ca1882a5131eecec602dbb46
    Cache-Control: no-cache

    {
        "code": 123,
        "name": "carlos",
        "active": true
    }

OBTENER TOKEN
    POST /api/rest/get_token/ HTTP/1.1
    Host: localhost:8000
    Content-Type: application/json
    Cache-Control: no-cache

    {
        "username": "admin",
        "password": "admin"
    }

## para crear token para existentes usuarios:

from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

## crea un nuevo token para cada usuario existente
for u in User.objects.all():
    Token.objects.get_or_create(user=u) 

## actualiza el token de todos los usuarios
for u in User.objects.all():
    t = Token.objects.get(user=u)
    t.delete()
    Token.objects.create(user=u)

## actualiza el token para un usuario especifico
u = User.objects.get(id=1)
Token.objects.get(user=u).delete()
Token.objects.create(user=u)

## crear un usuario de django con el shell
## http://tglei.blogspot.pe/2013/05/django-create-user-using-commandline.html
    $ python manage.py shell
    >>> from django.contrib.auth.models import User
    >>> user = User.objects.create_user('user001', 'user001@gmail.com', '123456') # username, email, passwd
    >>> user.first_name = 'first'
    >>> user.last_name = 'last'
    >>> user.save() # confirmar los cambios
    >>> exit() # salir del shell

## luego al llamar al servicio get_token "views.obtain_auth_token" con las credenciales registradas, se crea el token para el usuario

## cambiar el password a usuario django
## http://stackoverflow.com/questions/1873806/changing-password-in-django
entrar al shell
    >>> from django.contrib.auth.models import User
    >>> u = User.objects.get(username__exact='username')
    >>> u.set_password('admin')
    >>> u.save()

"""
urlsToken = [
    url(r'^get_token/', views.obtain_auth_token, name='token')
]




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
