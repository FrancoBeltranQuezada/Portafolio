from django.urls import path
from . import views
from .views import RegistrarBoleta
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('registrar_boleta/',(RegistrarBoleta.as_view()),name='registrar-boleta'),
]
