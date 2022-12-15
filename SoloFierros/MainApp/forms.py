from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class AutosFormulario(forms.Form):
    modelo = forms.CharField(max_length=50)
    marca = forms.CharField(max_length=50)
    fecha_fabricacion = forms.DateField()
    descripcion = forms.CharField(widget=forms.Textarea)
    precio = forms.IntegerField()
    imagen = forms.FileField()


class MotosFormulario(forms.Form):
    modelo = forms.CharField(max_length=50)
    marca = forms.CharField(max_length=50)
    fecha_fabricacion = forms.DateField()
    descripcion = forms.CharField(widget=forms.Textarea)
    precio = forms.IntegerField()
    imagen = forms.FileField()
