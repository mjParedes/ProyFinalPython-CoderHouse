from django.urls import path 
from AuthApp.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [

    path("register/", registrar_usuario, name="auth-registro"),
    path("perfil/editar/", editar_usuario, name="auth-editar"),
    path("perfil/avatar", agregar_avatar, name="auth-avatar"),

]