from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Reserva
from .forms import ReservaForm
# Create your views here.

class CrearReserva(CreateView):
    model = ReservaForm
    form_class = ReservaForm
    success_url = "/"
    template_name = "reserva/reserva_create.html"