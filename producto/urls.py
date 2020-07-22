from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('',login_required(views.home), name='producto-home'),
    path('about/',login_required(views.about), name='producto-about'),
    path('crear_producto/',login_required(views.crear_producto), name='crear_producto'),
    path('editar_producto/<str:id_producto>/', login_required(views.editar_producto), name='editar_producto'),
    path('eliminar_producto/<str:id_producto>/', login_required(views.eliminar_producto), name='eliminar_producto'),

]
