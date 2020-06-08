from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('',login_required(views.home), name='producto-home'),
    path('about/',login_required(views.about), name='producto-about'),
]
