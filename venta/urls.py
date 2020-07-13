from django.urls import path
from . import views
from .views import home, registrar_boleta
from django.contrib.auth.decorators import login_required


