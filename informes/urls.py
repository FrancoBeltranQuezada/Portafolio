from django.urls import path
from .views import reservas_pie,informes_view

urlpatterns = [
    path('',reservas_pie,name='informes'),
    path('informes',informes_view,name='dashboard')
]
