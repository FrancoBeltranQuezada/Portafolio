from django.urls import path
from . import views
from .views import OrderDeleteView,crearCustomer,EliminarCustomer,ListarCustomer
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('',login_required(views.tienda),name='store'),
    path('cart/',login_required(views.carrito),name='cart'),
    path('checkout/',login_required(views.checkout),name='checkout'),
    path('update_item/',login_required(views.updateItem),name='update_Item'),
    path('process_order/',login_required(views.processOrder),name='process_order'),
    path('listar_order/',login_required(views.listarOrder),name='listar_order'),
    path('listar_order/<int:pk>/delete/',login_required(OrderDeleteView.as_view()), name="order-delete"),
    path('customer/',login_required(crearCustomer),name="customer"),
    path('customer/<int:pk>/delete/',login_required(EliminarCustomer.as_view()),name="customer-delete"),
    path('customer/listar_customer',login_required(ListarCustomer),name="listar-customer")
]
