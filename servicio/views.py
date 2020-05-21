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

    if request.method == 'POST':
        formulario = ServicioForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "Guardado correctamente"

    return render (request,'servicio/registrar.html', data)


def actualizar_servicio (request, pk):
    data = {
        'form' : ServicioForm()
    }       

    return render (request, 'servicio/registrar.html', data)