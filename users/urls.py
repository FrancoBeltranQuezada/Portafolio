from django.urls import path, include
from .views import UserListView,UserDetailView,UserDeleteView,UpdateUserView,ErrorView,homeview
from .views import registrarEmpleado,EmpleadoListView,EmpleadoDetailView,EmpleadoDeleteView,UpdateEmpleadoView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('error',ErrorView,name='error'),
    path('',login_required(homeview), name='home'),

    #Urls vistas clientes
    path('gestion-clientes/',login_required(UserListView.as_view()),name="user-list"),
    path('gestion-clientes/<int:pk>/',login_required(UserDetailView.as_view()),name="user-detail"),
    path('gestion-clientes/<int:pk>/delete/',login_required(UserDeleteView.as_view()),name="user-delete"),
    path('gestion-clientes/<int:pk>/update/',login_required(UpdateUserView),name='user-update'),
    
    #Urls vistas empleados
    path('gestion-empleados/new',login_required(registrarEmpleado),name='registrar-empleado'),
    path('gestion-empleados/',login_required(EmpleadoListView.as_view()),name='empleado-list'),
    path('gestion-empleados/<int:pk>/',login_required(EmpleadoDetailView.as_view()),name='empleado-detail'),
    path('gestion-empleados/<int:pk>/delete/',login_required(EmpleadoDeleteView.as_view()),name="empleado-delete"),
    path('gestion-empleados/<int:pk>/update/',login_required(UpdateEmpleadoView),name='empleado-update'),
    
]   