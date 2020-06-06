from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('',login_required(views.index), name='proveedor-home'),
    path('aboutt/',login_required(views.aboutt), name='proveedor-about'),
    path('crear_proveedor/',login_required(views.crear_proveedor),name='crear_proveedor'),
    path('editar_proveedor/<str:id_prov>/', login_required(views.editar_proveedor), name='editar_proveedor'),
    path('eliminar_proveedor/<str:id_prov>/', login_required(views.eliminar_proveedor), name='eliminar_proveedor'),
    path('eliminar/<int:id_prov>', login_required(views.eliminar_proveedor), name='eliminar_proveedor'),
  
]
