 
from apprest.viewsets import LibroViewSet, AutorViewSet
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r'libros', LibroViewSet, base_name='libro')
router.register(r'autores', AutorViewSet, base_name='autor')

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