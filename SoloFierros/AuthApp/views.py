from django.shortcuts import render, redirect
from AuthApp.models import *
from AuthApp.forms import FormularioDeRegistro, EditarUsuario, AvatarUsuario
from django.contrib.auth.decorators import login_required

# Create your views here.


def registrar_usuario(request):

    if request.method == "POST":

        formulario = FormularioDeRegistro(request.POST)

        if formulario.is_valid():

            formulario.save()
            return redirect("inicio")

        else:
            return render(request, "AuthApp/registro_usuario.html",{"form": formulario, "errors": formulario.errors})

    formulario = FormularioDeRegistro()
    return render(request, "AuthApp/registro_usuario.html", {"form": formulario})


@login_required

def editar_usuario(request):

    usuario = request.user

    if request.method == "POST":

        formulario = EditarUsuario(request.POST)

        if formulario.is_valid():

            data = formulario.cleaned_data
            usuario.email = data["email"]
            usuario.nombre = data["nombre"]
            usuario.apellido = data["apellido"]

            usuario.save()

            return redirect("inicio")

        else:

            return render(request, "AuthApp/editar_usuario.html",{"form": formulario, "errors": formulario.errors})

    else:

        formulario = EditarUsuario(initial={"email": usuario.email, "nombre": usuario.nombre, "apellido": usuario.apellido})
    
    return render (request, "AuthApp/editar_usuario.html", {"form": formulario})
        
@login_required

def agregar_avatar(request):

    if request.method == "POST":
        
        formulario = AvatarUsuario(request.POST, files=request.FILES)
        print(request.FILES, request.POST)

        if formulario.is_valid():

            data = formulario.cleaned_data
            usuario = request.user
            avatar = Avatar(usuario=usuario, imagen=data["imagen"])

            avatar.save()

            return redirect("inicio")

        else:

            return render(request, "AuthApp/agregar_avatar.html",{"form": formulario, "errors": formulario.errors})

    formulario = AvatarUsuario()
    return render(request, "AuthApp/agregar_avatar.html", {"form": formulario})
    

# Create your views here.
