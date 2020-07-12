from django.shortcuts import render
from django.http import HttpResponse
from .forms import DetalleBoletaForm, BoletaMultiForm
from servicio.models import Servicio
from django.shortcuts import redirect
from .models import Boleta, DetalleBoleta
from datetime import datetime
from datetime import date


from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
#from .decorators import unaunthenticated_user, allowed_users, admin_only
# Create your views here.



def home (request):
    
    data = {'time':datetime.now()}
    return render(request,'boleta/registro_boleta.html',data )    


def registrar_boleta (request):

    now = datetime.now()
    format = now.strftime('%d-%m-%Y')

    data = {
        'form': BoletaMultiForm(),
        'time': format
    }

    if request.method == 'POST':
        formulario = BoletaMultiForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "Guardado correctamente"
        else:
            data['mensaje'] = "Boleta no se pudo guardar correctamente"


    return render (request,'boleta/registro_boleta.html', data)