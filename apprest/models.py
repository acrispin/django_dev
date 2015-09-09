from django.db import models
from django.conf import settings

class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)

    def __unicode__(self):              # __str__ on Python 3
        return self.nombre
    
class Libro(models.Model):
    nombre = models.CharField(max_length=100)
    editorial = models.CharField(max_length=100)
    genero = models.CharField(max_length=100)
    autor = models.ForeignKey(Autor)

    def __unicode__(self):              # __str__ on Python 3
        return self.nombre

UPLOAD_DIRS = getattr(settings, 'UPLOAD_DIRS', '')

class File(models.Model):
    pathfile = models.FileField(upload_to=UPLOAD_DIRS)
    reg_date = models.DateTimeField(auto_now_add=True, null=True)    
    mod_date = models.DateTimeField(auto_now=True, null=True)

    def __unicode__(self):              # __str__ on Python 3
        if self.pathfile.name.rfind('/') > 0:
            return self.pathfile.name[self.pathfile.name.rfind('/') + 1:]