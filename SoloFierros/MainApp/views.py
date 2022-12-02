from django.shortcuts import render
from MainApp.models import *

# Create your views here.

def vista_inicio(request):
    return render(request, "MainApp/index.html")

def vista_nosotros(request):
    return render(request, "MainApp/about.html")

def busqueda_autos_resultados(request):

    nombre_automovil = request.GET["nombre_automovil"]
    automovil = Automovil.objects.filter(nombre__icontains=nombre_automovil)

    return render(request, "MainApp/busqueda_autos_resultados.html", {"automovil": automovil})
