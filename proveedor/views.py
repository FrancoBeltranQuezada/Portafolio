from django.shortcuts import redirect, render
from .models import prov
from django.http import HttpResponse
from .forms import ProvForm

# Create your views here.


def index (request):
    provs = prov.objects.all()
    contexto = {
        'provs':provs

    }
    return render(request,'proveedor/templates/index.html',contexto)

def aboutt (request):
    return render(request,'proveedor/templates/aboutt.html')


def crear_proveedor (request):
    data = {
        'form': ProvForm()
    }

    if request.method == 'POST':
        formulario = ProvForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "Guardado correctamente"

    return render (request,'proveedor/templates/crear.html', data)

def editar_proveedor(request, id_prov):
    provs = prov.objects.get(id_prov=id_prov)
    if request.method == 'GET':
        formulario = ProvForm(instance=provs)
        context = {
            'form':formulario
        }
    else:
        formulario = ProvForm(request.POST, instance = provs)
        context = {
            'form':formulario
        }
        if formulario.is_valid():
            formulario.save()
            return redirect('proveedor-home')
            

    return render(request,'proveedor/templates/crear.html',context)


