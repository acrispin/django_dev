from django.db import models

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
