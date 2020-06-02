from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='proveedor-home'),
    path('aboutt/',views.aboutt, name='proveedor-about'),
    path('crear_proveedor/',views.crear_proveedor,name='crear_proveedor'),
    path('editar_proveedor/<str:id_prov>/', views.editar_proveedor, name='editar_proveedor'),
    path('eliminar_proveedor/<str:id_prov>/', views.eliminar_proveedor, name='eliminar_proveedor'),
  
]
