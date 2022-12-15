from django.db import models

# Create your models here.
class Automovil(models.Model):
    modelo = models.CharField(max_length=50)
    marca = models.CharField(max_length=50)
    fecha_fabricacion = models.DateField()
    descripcion = models.TextField(max_length=1000)
    precio = models.IntegerField()
    imagen = models.FileField(upload_to='images', null=True)

    def __str__(self):
        return f"{self.marca} -  {self.modelo}"


class Moto(models.Model):
    modelo = models.CharField(max_length=50)
    marca = models.CharField(max_length=50)
    fecha_fabricacion = models.DateField()
    descripcion = models.TextField(max_length=1000)
    precio = models.IntegerField()
    imagen = models.FileField(upload_to='images', null=True)

    def __str__(self):
        return f"{self.marca} -  {self.modelo}"


class Sucursal(models.Model):
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=100)
    telefono = models.IntegerField()

    def __str__(self):
        return f"Sucursal: {self.nombre}"

