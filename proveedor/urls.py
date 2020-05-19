from django.urls import path
from . import views

urlpatterns = [
    path('proveedor/',views.index, name='proveedor-home'),
    path('aboutt/',views.aboutt, name='proveedor-about'),
]
