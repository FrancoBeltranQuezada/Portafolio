from django.urls import path, include
from .views import UserListView,UserDetailView,UserDeleteView,UpdateUserView,ErrorView,homeview
from .views import registrarEmpleado,EmpleadoListView,EmpleadoDetailView,EmpleadoDeleteView,UpdateEmpleadoView

urlpatterns = [
    path('error',ErrorView,name='error'),
    path('',homeview, name='home'),

    #Urls vistas clientes
    path('gestion-clientes/',UserListView.as_view(),name="user-list"),
    path('gestion-clientes/<int:pk>/',UserDetailView.as_view(),name="user-detail"),
    path('gestion-clientes/<int:pk>/delete/',UserDeleteView.as_view(),name="user-delete"),
    path('gestion-clientes/<int:pk>/update/',UpdateUserView,name='user-update'),
    
    #Urls vistas empleados
    path('gestion-empleados/new',registrarEmpleado,name='registrar-empleado'),
    path('gestion-empleados/',EmpleadoListView.as_view(),name='empleado-list'),
    path('gestion-empleados/<int:pk>/',EmpleadoDetailView.as_view(),name='empleado-detail'),
    path('gestion-empleados/<int:pk>/delete/',EmpleadoDeleteView.as_view(),name="empleado-delete"),
    path('gestion-empleados/<int:pk>/update/',UpdateEmpleadoView,name='empleado-update'),
    
]   