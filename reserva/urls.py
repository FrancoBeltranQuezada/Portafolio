from django.urls import path
from .views import CrearReserva,ListarReserva,EliminarReserva,UpdateReservaView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('gestion-reserva/crear-reserva',login_required(CrearReserva.as_view()),name='crear-reserva'),
    path('gestion-reserva/',login_required(ListarReserva.as_view()),name='listar-reserva'),
    path('gestion-reserva/<int:pk>/delete/',login_required(EliminarReserva.as_view()),name='elminar-reserva'),
    path('gestion-reserva/<int:pk>/update/',login_required(UpdateReservaView),name='actualizar-reserva'),

]
