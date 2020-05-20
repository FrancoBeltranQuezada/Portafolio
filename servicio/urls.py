from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='servicio-home'),
    path('about/',views.about, name='servicio-about'),
    path('registrar/',views.registrar_servicio, name= 'registrar-servicio'),
]
