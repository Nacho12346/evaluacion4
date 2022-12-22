from unittest.util import _MAX_LENGTH
from django.db import models
from .elecciones import opciones


class Institucion(models.Model):
    institucion = models.CharField(max_length=50)
    def str(self):
        return self.institucion

class Inscritos(models.Model): 
    id = models.AutoField(primary_key=True)
    nombreCompleto  = models.CharField(max_length=50)
    telefono = models.CharField(max_length=20)
    fechainscripcion = models.DateField()
    institucion = models.ForeignKey(Institucion, on_delete= models.CASCADE)
    horainscripcion = models.TimeField()
    estados = models.CharField(max_length=50, choices= opciones)
    observacion = models.CharField(max_length=50, blank= True)