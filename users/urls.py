from django.urls import path, include
from .views import UserListView,UserDetailView,UserCreateView,UserUpdateView,UserDeleteView

urlpatterns = [
    path('gestion-clientes/',UserListView.as_view(),name="user-list"),
    path('gestion-clientes/<int:pk>/',UserDetailView.as_view(),name="user-detail"),
    path('gestion-clientes/new/',UserCreateView.as_view(),name="user-create"),
    path('gestion-clientes/<int:pk>/update/',UserUpdateView.as_view(),name="user-update"),
   # path('gestion-clientes/<int:pk>/delete/',del_user,name="user-delete"),
    path('gestion-clientes/<int:pk>/delete/',UserDeleteView.as_view(),name="user-delete"),
]   