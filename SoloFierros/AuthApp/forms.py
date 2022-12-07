from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class FormularioDeRegistro(UserCreationForm):

    nombre = forms.CharField(label="Nombre")
    apellido = forms.CharField(label="Apellido")
    email = forms.EmailField(label="Correo electrónico")
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirme el password", widget=forms.PasswordInput)


    class Meta:

        model = User
        fields = ["username", "nombre", "apellido", "email", "password1", "password2"]


class EditarUsuario(UserCreationForm):

    nombre = forms.CharField(label="Nombre")
    apellido = forms.CharField(label="Apellido")
    email = forms.EmailField(label="Correo electrónico")
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput, required=False)
    password2 = forms.CharField(label="Confirme el password", widget=forms.PasswordInput, required=False)

    class Meta:

        model = User
        fields = ["username", "nombre", "apellido", "email", "password1", "password2"]
        help_texts = {"email": "Indica un correo electronico que uses habitualmente", "nombre": "", "apellido": "", "password1": ""}


class AvatarUsuario(forms.Form):
    
    imagen = forms.ImageField()