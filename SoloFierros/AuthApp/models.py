from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Registrar(models.Model):
    nombre_usuario = models.CharField(max_length=60)
    email_usuario = models.EmailField(max_length=80)
    password_usuario = models.CharField(max_length=25)

    def __str__(self):
        return f"{self.nombre_usuario} || {self.email_usuario}"


class Avatar(models.Model):

    usuario = models.ForeignKey(User,on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to= "avatares", null=True, blank=True)