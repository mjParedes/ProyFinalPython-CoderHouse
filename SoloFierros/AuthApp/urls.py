from django.urls import path 
from AuthApp.views import *
from MainApp.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [

    path("accounts/signup/", registrar_usuario, name="auth-registro"),
    path("accounts/profile/editar/", editar_usuario, name="auth-editar"),
    path("accounts/profile/avatar", agregar_avatar, name="auth-avatar"),
    path("accounts/login/", iniciar_sesion, name="auth-login"),
    path("logout/", LogoutView.as_view(template_name="AuthApp/logout.html"), name="auth-logout"),


]