from django.shortcuts import render, redirect
from MainApp.models import *
from MainApp.forms import AutosFormulario, MotosFormulario
from django.views.generic import ListView, DetailView, UpdateView, DeleteView


# Create your views here.

def vista_inicio(request):
    return render(request, "MainApp/index.html")

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

    return render(request, "MainApp/autos_formulario.html", {"formulario":formulario})

class Autos(ListView):

    model = Automovil
    template_name = "MainApp/autos.html"

class AutosDelete(DeleteView):

    model = Automovil
    success_url = "/main/autos/"


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

            auto.save()

            return redirect ("autos")

        else:
            return render(request, "MainApp/editar_autos.html", {"formulario": formulario, "errores": formulario.errors})
        
    else:
        formulario = AutosFormulario(initial={"modelo": auto.modelo, "marca":auto.marca})

        return render(request, "MainApp/editar_autos.html", {"formulario": formulario, "errores": ""})

class AutosDetail(DetailView):

    model = Automovil
    template_name = "MainApp/autos_detail.html"



def motos_formulario(request):
    if request.method == "POST":
        formulario = MotosFormulario(request.POST)
        print(formulario)

        if formulario.is_valid():
            data = formulario.cleaned_data

            moto = Moto(
                modelo = data["modelo"],
                marca = data["marca"],
                fecha_fabricacion = data["fecha_fabricacion"],
                descripcion = data["descripcion"],
                precio = data["precio"],
            )

            moto.save()
            return render(request,"MainApp/motos.html")

    else:
        formulario = MotosFormulario() 

    return render(request, "MainApp/motos_formulario.html", {"formulario":formulario})

class Motos(ListView):

    model = Moto
    template_name = "MainApp/motos.html"




