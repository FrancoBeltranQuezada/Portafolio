from django.shortcuts import render
from django.http import HttpResponse
from .forms import DetalleBoletaForm, BoletaMultiForm
from servicio.models import Servicio
from django.shortcuts import redirect
from .models import Boleta, DetalleBoleta
from datetime import datetime


from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
#from .decorators import unaunthenticated_user, allowed_users, admin_only
# Create your views here.


class RegistrarBoleta(CreateView):
    model = DetalleBoleta
    form_class = BoletaMultiForm
    
    template_name = "boleta/registro_boleta.html"



def a_view(request):
    return render_to_response("boleta/registro.html", {
        'time':datetime.now(),
        }, context_instance=RequestContext(request))    

    
