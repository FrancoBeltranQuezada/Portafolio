from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='producto-home'),
    path('about/',views.home, name='producto-about'),
]
