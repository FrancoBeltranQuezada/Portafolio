from django.urls import path
from .views import reservas_pie,informes_view
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('',login_required(reservas_pie),name='informes'),
    path('informes',login_required(informes_view),name='dashboard')
]
