from django.urls import path 
from MainApp.views import *

urlpatterns = [
    path("", vista_inicio, name="inicio"),
    path("about/", vista_nosotros, name="nosotros"),
    path("busqueda/autos/resultados/", busqueda_autos_resultados, name="busqueda-autos-resultados"),

]