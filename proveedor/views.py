from django.shortcuts import redirect, render
from .models import prov
from django.http import HttpResponse
from .forms import ProvForm
from .decorators import allowed_users

# Create your views here.

@allowed_users(allowed_roles=['admin', 'empleado'])
def index (request):
    provs = prov.objects.all()
    contexto = {
        'provs':provs

    }
    return render(request,'proveedor/templates/index.html',contexto)


@allowed_users(allowed_roles=['admin', 'empleado'])
def aboutt (request):
    return render(request,'proveedor/templates/aboutt.html')



@allowed_users(allowed_roles=['admin', 'empleado'])
def crear_proveedor (request):
    data = {
        'form': ProvForm()
    }

    if request.method == 'POST':
        formulario = ProvForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "Guardado correctamente"
        return redirect('proveedor-home')

    return render (request,'proveedor/templates/crear.html', data)


@allowed_users(allowed_roles=['admin', 'empleado'])
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


@allowed_users(allowed_roles=['admin', 'empleado'])
def eliminar_proveedor(request, id_prov):
    provs = prov.objects.get(id_prov=id_prov)

    if request.method == 'POST':
        provs.delete()
        return redirect('proveedor-home')
    return render(request, 'proveedor/templates/eliminar.html',{'provs':provs})


