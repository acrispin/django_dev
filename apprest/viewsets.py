from .models import Libro, Autor, File
from .serializers import LibroSerializer, AutorSerializer, FileSerializer
# from rest_framework import viewsets
from rest_framework.viewsets import ModelViewSet
 
class LibroViewSet(ModelViewSet): 
    serializer_class = LibroSerializer
    queryset = Libro.objects.all()
 
class AutorViewSet(ModelViewSet): 
    serializer_class = AutorSerializer
    queryset = Autor.objects.all()

class FileViewSet(ModelViewSet): 
    queryset = File.objects.all()
    serializer_class = FileSerializer