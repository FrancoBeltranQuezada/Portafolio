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
