from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('',(views.home), name='producto-home'),
    path('about/',(views.about), name='producto-about'),
    path('crear_producto/',views.crear_producto, name='crear_producto'),
    path('editar_producto/<str:id_producto>/', views.editar_producto, name='editar_producto'),
    path('eliminar_producto/<str:id_producto>/', views.eliminar_producto, name='eliminar_producto'),

]
