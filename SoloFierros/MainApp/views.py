from django.shortcuts import render, redirect
from MainApp.models import *
from AuthApp.models import *
from MainApp.forms import AutosFormulario, MotosFormulario
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required



# Create your views here.

def vista_inicio(request):
     if request.user.is_authenticated:
         imagen_model = Avatar.objects.filter(usuario= request.user.id)[0]
         imagen_url = imagen_model.imagen.url
     else:
         imagen_url = ""
     return render(request, "MainApp/index.html", {"imagen_url": imagen_url})


#<<<<<<< HEAD

class Sucursales(LoginRequiredMixin, ListView):

    model = Sucursal
    template_name = "MainApp/sucursales.html"


@login_required
#=======
#>>>>>>> a2b226bf9fad204fa58485241b254eeb97288e50
def vista_nosotros(request):
    return render(request, "MainApp/about.html")

def autos_formulario(request):
    if request.method == "POST":
        formulario = AutosFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data

            auto = Automovil(
                
                modelo = data["modelo"],
                marca = data["marca"],
                fecha_fabricacion = data["fecha_fabricacion"],
                descripcion = data["descripcion"],
                precio = data["precio"],
                #imagen = data["imagen"],
            )

            auto.save()
            return render(request,"MainApp/autos.html")

    else:
        formulario = AutosFormulario() 

    return render(request, "MainApp/autos_formulario.html", {"formulario": formulario})

class Autos(LoginRequiredMixin, ListView):
    
    model = Automovil
    template_name = "MainApp/autos.html"

def borrar_auto(request, id):
    auto = Automovil.objects.get(id=id)
    auto.delete()

    return redirect("autos")

def editar_autos(request, id):
    auto = Automovil.objects.get(id=id)

    

    if request.method == "POST":
        formulario = AutosFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data

            auto.modelo = data["modelo"]
            auto.marca = data["marca"]
            auto.precio = data["precio"]
            auto.descripcion = data["descripcion"]
            auto.fecha_fabricacion = data["fecha_fabricacion"]

            auto.save()

            return redirect ("autos")

        else:
            return render(request, "MainApp/editar_autos.html", {"formulario": formulario, "errores": formulario.errors})
        
    else:
        formulario = AutosFormulario(initial={"modelo": auto.modelo, "marca":auto.marca, "descripcion": auto.descripcion, "precio": auto.precio})

        return render(request, "MainApp/editar_autos.html", {"formulario": formulario, "errores": ""})

class AutosDetail(DetailView):

    model = Automovil
    template_name = "MainApp/autos_detail.html"





def motos_formulario(request):
    if request.method == "POST":
        formulario = MotosFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data

            moto = Moto(

                modelo = data["modelo"],
                marca = data["marca"],
                fecha_fabricacion = data["fecha_fabricacion"],
                descripcion = data["descripcion"],
                precio = data["precio"],
                imagen = data["imagen"],

            )

            moto.save()
            return render(request,"MainApp/motos.html")

    else:
        formulario = MotosFormulario() 

    return render(request, "MainApp/motos.html", {"formulario":formulario})

class Motos(LoginRequiredMixin, ListView):

    model = Moto
    template_name = "MainApp/motos.html"
    
def editar_motos(request, id):
    moto = Moto.objects.get(id=id)

    

    if request.method == "POST":
        formulario = MotosFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data

            moto.modelo = data["modelo"]
            moto.marca = data["marca"]
            moto.precio = data["precio"]
            moto.descripcion = data["descripcion"]
            moto.fecha_fabricacion = data["fecha_fabricacion"]

            moto.save()

            return redirect ("motos")

        else:
            return render(request, "MainApp/editar_motos.html", {"formulario": formulario, "errores": formulario.errors})
        
    else:
        formulario = MotosFormulario(initial={"modelo": moto.modelo, "marca":moto.marca, "descripcion": moto.descripcion, "precio": moto.precio})

        return render(request, "MainApp/editar_motos.html", {"formulario": formulario, "errores": ""})

class MotosDetail(DetailView):

    model = Moto
    template_name = "MainApp/motos_detail.html"

def borrar_moto(request, id):
    moto = Moto.objects.get(id=id)
    moto.delete()

    return redirect("motos")






@login_required
def resultado_busqueda(request):

    marca_auto = request.GET["vehiculo"]
    autos = Automovil.objects.filter(marca__icontains=marca_auto)
    motos = Moto.objects.filter(marca__icontains=marca_auto)

    return render(request, "MainApp/resultados_busquedas.html", {"auto": autos, "moto": motos})
