from django.db import models

# Create your models here.
class Taxi(models.Model):
    nombre = models.CharField(max_length=20)
    chofer = models.CharField(max_length=60)
    capacidad = models.IntegerField()
    telefono = models.CharField(max_length=10)
    tipo = models.CharField(max_length=20)
    
    def __str__(self):
        return self.nombre

    def __unicode__(self):
        return self.nombre
    
class Trabajador(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.TextField()
    telefono = models.CharField(max_length=10)
    

    def __str__(self):
        return self.nombre

    def __unicode__(self):
        return self.nombre

class Viaje(models.Model):
    tipo_viaje = models.CharField(max_length=25)
    taxi = models.ForeignKey(Taxi, on_delete = models.CASCADE)
    Trabajador = models.ManyToManyField(Trabajador)
    fecha = models.DateField()
    hora = models.TimeField()
    def __str__(self):
        return self.tipo_viaje

    def __unicode__(self):
        return self.tipo_viaje
