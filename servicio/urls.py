from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.home, name='servicio-home'),
    path('about/',views.about, name='servicio-about'),
    path('registrar/',views.registrar_servicio, name= 'registrar-servicio'),
    path('actualizar_servicio/<str:pk>', views.actualizar_servicio, name='actualizar-servicio'),
]
