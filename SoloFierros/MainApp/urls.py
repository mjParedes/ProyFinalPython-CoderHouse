from django.urls import path 
from MainApp.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    
    path("", vista_inicio, name="inicio"),
    path("about/", vista_nosotros, name="nosotros"),
    path("autos/", Autos.as_view(), name="autos"),
    path("autos/detalle/<pk>/", AutosDetail.as_view(), name="autos-detail"),
    path("autos/borrar/<id>/", borrar_auto, name="autos-borrar"),
    path("autos/actualizar/<id>/", editar_autos, name="autos-editar"),
    path("autos/borrar/<pk>/", AutosDelete.as_view(), name="autos-delete"),

   
    path("motos/", Motos.as_view(), name="motos"),
    path("motos/agregar/", motos_formulario, name="motos-nuevo"),
    path("autos/agregar/", autos_formulario, name="autos-nuevo"),


]