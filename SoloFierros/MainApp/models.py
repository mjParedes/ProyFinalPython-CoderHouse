from django.db import models

# Create your models here.
class Automovil(models.Model):
    modelo = models.CharField(max_length=50)
    marca = models.CharField(max_length=50)
    origen = models.CharField(max_length=50)
    fecha_fabricacion = models.DateField()
    descripcion = models.TextField(max_length=1000)
    precio = models.IntegerField()

    def __str__(self):
        return f"Modelo: {self.modelo} || {self.marca}"

 