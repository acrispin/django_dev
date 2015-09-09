# from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Libro, Autor, File
 
class LibroSerializer(ModelSerializer):
    class Meta:
        model = Libro
        fields = ('id', 'nombre', 'editorial', 'genero', 'autor',)
 
class AutorSerializer(ModelSerializer):
    class Meta:
        model = Autor
        fields = ('id', 'nombre', 'apellido',)

class FileSerializer(ModelSerializer):
    class Meta:
        model = File