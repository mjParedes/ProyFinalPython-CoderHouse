from django.shortcuts import render

# Create your views here.

def vista_inicio(request):
    return render(request, "MainApp/index.html")
