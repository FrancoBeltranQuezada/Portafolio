from django.urls import path
from . import views

urlpatterns = [
    #path('home/',views.home, name='servicio-home'),
    path('about/',views.about, name='servicio-about'),
    path('registrar/',views.registrar_servicio, name= 'registrar-servicio'),
    path('actualizar_servicio/<int:id_servicio>', views.actualizar_servicio, name='actualizar-servicio'),
    path('home/',views.listar_servicio, name= 'listar-servicio'),
    path('eliminar/<int:id_servicio>', views.eliminar_servicio, name='eliminar-servicio'),
]
