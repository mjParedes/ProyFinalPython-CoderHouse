from django.shortcuts import render
from MainApp.models import *
from MainApp.forms import AutosFormulario, MotosFormulario

# Create your views here.

def vista_inicio(request):
    return render(request, "MainApp/index.html")

def vista_nosotros(request):
    return render(request, "MainApp/about.html")

def busqueda_autos_resultados(request):

    nombre_automovil = request.GET["nombre_automovil"]
    automovil = Automovil.objects.filter(nombre__icontains=nombre_automovil)

    return render(request, "MainApp/busqueda_autos_resultados.html", {"automovil": automovil})

def motos_formulario(request):
    if request.method == "POST":
        formulario = MotosFormulario(request.POST)
        print(formulario)

        if formulario.is_valid:
            data = formulario.cleaned_data

            moto = Moto(
                modelo = data["modelo"],
                marca = data["marca"],
                fecha_fabricacion = data["fecha_fabricacion"],
                descripcion = data["descripcion"],
                precio = data["precio"],
            )

            moto.save()
            return render(request,"MainApp/index.html")

    else:
        formulario = MotosFormulario() 

    return render(request, "MainApp/motos_formulario.html", {"formulario":formulario})
    
   

def autos_formulario(request):
    if request.method == "POST":
        formulario = AutosFormulario(request.POST)
        print(formulario)

        if formulario.is_valid:
            data = formulario.cleaned_data

            auto = Automovil(
                modelo = data["modelo"],
                marca = data["marca"],
                fecha_fabricacion = data["fecha_fabricacion"],
                descripcion = data["descripcion"],
                precio = data["precio"],
            )

            auto.save()
            return render(request,"MainApp/index.html")

    else:
        formulario = AutosFormulario() 

    return render(request, "MainApp/autos_formulario.html", {"formulario":formulario})
    