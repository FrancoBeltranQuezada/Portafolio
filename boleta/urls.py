from django.urls import path
from . import views
from .views import home, registrar_boleta
from django.contrib.auth.decorators import login_required


urlpatterns = [
    #path('registrar_boleta/',(RegistrarBoleta.as_view()),name='registrar-boleta'),
    path('registrar_boleta/',views.registrar_boleta,name='registrar-boleta'),
]
