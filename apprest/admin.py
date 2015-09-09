from django.contrib import admin
from .models import Autor, Libro, File

admin.site.register(Autor)
admin.site.register(Libro)
admin.site.register(File)
