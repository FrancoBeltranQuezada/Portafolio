from django.urls import path
from .views import reservas_pie

urlpatterns = [
    path('',reservas_pie,name='informes')
]
