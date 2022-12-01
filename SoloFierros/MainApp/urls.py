from django.urls import path 
from MainApp.views import *

urlpatterns = [
    path("inicio/", vista_inicio)
]