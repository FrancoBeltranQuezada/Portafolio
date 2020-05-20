from django.shortcuts import render
from django.http import HttpResponse
from .forms import ServicioForm

# Create your views here.

def home (request):
    return render(request,'servicio/home.html')


def about(request): 
    return render(request,'servicio/about.html')     


def registrar_servicio (request):
    data = {
        'form': ServicioForm()
    }
    return render (request,'servicio/registrar.html', data)