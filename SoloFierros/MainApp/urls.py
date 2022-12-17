from django.urls import path 
from MainApp.views import *


urlpatterns = [
    
    path("", vista_inicio, name="inicio"),
    path("about/", vista_nosotros, name="nosotros"),
    path("sucursales/", Sucursales.as_view(), name="sucursales"),
    
    path("autos/", Autos.as_view(), name="autos"),
    path("autos/detalle/<pk>/", AutosDetail.as_view(), name="autos-detail"),
    path("autos/borrar/<id>/", borrar_auto, name="autos-borrar"),
    path("autos/actualizar/<id>/", editar_autos, name="autos-editar"),
    path("autos/agregar/", autos_formulario, name="autos-nuevo"),
   
    path("motos/", Motos.as_view(), name="motos"),
    path("motos/agregar/", motos_formulario, name="motos-nuevo"),
    path("motos/detalle/<pk>/", MotosDetail.as_view(), name="motos-detail"),
    path("motos/borrar/<id>/", borrar_moto, name="moto-borrar"),
    path("motos/actualizar/<id>/", editar_motos, name="moto-editar"),
    


    path("buscar/resultados/", resultado_busqueda, name="buscar-resultados"),

] 