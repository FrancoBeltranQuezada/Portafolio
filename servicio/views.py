from django.shortcuts import render
from django.http import HttpResponse
from .forms import ServicioForm
from servicio.models import Servicio
from django.shortcuts import redirect
from .decorators import unaunthenticated_user, allowed_users, admin_only

# Create your views here.
@admin_only
def home (request):
    return render(request,'servicio/home.html')

@admin_only
def about(request): 
    return render(request,'servicio/about.html')     

@admin_only
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

@admin_only
def actualizar_servicio(request, id_servicio):
    servicio = Servicio.objects.get(id_servicio=id_servicio)

    if request.method == 'GET':
        form = ServicioForm(instance = servicio)
    else:
        form = ServicioForm(request.POST, instance = servicio)
        if form.is_valid():
            form.save()
           
            return redirect ('listar-servicio')   
    contexto ={'form' : form}         
    return render (request, 'servicio/registrar.html', contexto)

@admin_only
def listar_servicio(request):
    servicio = Servicio.objects.all().order_by('id_servicio')
    contexto ={'servicios' : servicio}   
    return render (request, 'servicio/home.html', contexto)


@admin_only
def eliminar_servicio(request, id_servicio):
    servicio = Servicio.objects.get(id_servicio=id_servicio)

    if request.method == 'POST':
        servicio.delete()
        return redirect('listar-servicio')

    
    return render (request, 'servicio/eliminar.html', {'servicio':servicio})