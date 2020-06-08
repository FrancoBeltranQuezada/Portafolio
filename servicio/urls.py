from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    #path('home/',views.home, name='servicio-home'),
    path('about/',login_required(views.about), name='servicio-about'),
    path('registrar/',login_required(views.registrar_servicio), name= 'registrar-servicio'),
    path('actualizar_servicio/<int:id_servicio>', login_required(views.actualizar_servicio), name='actualizar-servicio'),
    path('home/',login_required(views.listar_servicio), name= 'listar-servicio'),
    path('eliminar/<int:id_servicio>', login_required(views.eliminar_servicio), name='eliminar-servicio'),
]
