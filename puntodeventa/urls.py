from django.urls import path
from . import views


urlpatterns = [
    path('',views.tienda,name='store'),
    path('cart/',views.carrito,name='cart'),
    path('checkout/',views.checkout,name='checkout'),
    path('update_item/',views.updateItem,name='update_Item'),
    path('process_order/',views.processOrder,name='process_order')
]
