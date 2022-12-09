from django.urls import path 
from AuthApp.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [

    path("register/", registrar_usuario, name="auth-registro"),
    path("perfil/editar/", editar_usuario, name="auth-editar"),
    path("perfil/avatar", agregar_avatar, name="auth-avatar"),
    path("login/", iniciar_sesion, name="auth-login"),
    path("logout/", LogoutView.as_view(template_name="AuthApp/logout.html"), name="auth-logout"),

]