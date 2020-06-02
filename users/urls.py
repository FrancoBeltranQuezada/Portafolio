from django.urls import path, include
from .views import UserListView,UserDetailView,UserCreateView,UserDeleteView,UserUpdateProfile,UpdateUser,homeview,ErrorView,registrarEmpleado,EmpleadoListView
from .views import EmpleadoDetailView,EmpleadoDeleteView,EmpleadoUpdateProfile

urlpatterns = [
    path('gestion-clientes/',UserListView.as_view(),name="user-list"),
    path('gestion-clientes/<int:pk>/',UserDetailView.as_view(),name="user-detail"),
    path('gestion-clientes/new/',UserCreateView.as_view(),name="user-create"),
    path('gestion-clientes/<int:pk>/update/',UserUpdateProfile,name="user-update"),
   # path('gestion-clientes/<int:pk>/delete/',del_user,name="user-delete"),
    path('gestion-clientes/<int:pk>/delete/',UserDeleteView.as_view(),name="user-delete"),
    path('error',ErrorView,name='error'),
    path('',homeview, name='home'),

    path('gestion-empleado/<int:pk>/',EmpleadoDetailView.as_view(),name="empleado-detail"),
    path('gestion-empleado/new',registrarEmpleado,name='registrar-empleado'),
    path('gestion-empleado/',EmpleadoListView.as_view(),name="empleado-list"),
    path('gestion-empleado/<int:pk>/delete/',EmpleadoDeleteView.as_view(),name="empleado-delete"),
    path('gestion-empleado/<int:pk>/update/',EmpleadoUpdateProfile,name="empleado-update"),
    
]   