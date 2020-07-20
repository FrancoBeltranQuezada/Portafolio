from django.urls import path
from . import views
from .views import OrderDeleteView


urlpatterns = [
    path('',views.tienda,name='store'),
    path('cart/',views.carrito,name='cart'),
    path('checkout/',views.checkout,name='checkout'),
    path('update_item/',views.updateItem,name='update_Item'),
    path('process_order/',views.processOrder,name='process_order'),
    path('listar_order/',views.listarOrder,name='listar_order'),
    path('listar_order/<int:pk>/delete/',OrderDeleteView.as_view(), name="order-delete"),
]
