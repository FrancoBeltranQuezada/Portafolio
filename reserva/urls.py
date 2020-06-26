from django.urls import path
from .views import CrearReserva
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('crear-reserva/',login_required(CrearReserva.as_view()),name='crear-reserva')
]
