from django.shortcuts import render
from django.http import HttpResponse
from .forms import DetalleBoletaForm, BoletaMultiForm
from servicio.models import Servicio
from django.shortcuts import redirect
from .models import Boleta, DetalleBoleta
from datetime import datetime
from datetime import date


from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
#from .decorators import unaunthenticated_user, allowed_users, admin_only
# Create your views here.


def add_to_cart(request, **kwargs):
    # get the user profile
    # filter products by id
    servicio = Servicio.objects.filter(id=kwargs.get('item_id', "")).first()
    # check if the user already owns this product
    if product in request.user.profile.ebooks.all():
        messages.info(request, 'You already own this ebook')
        return redirect(reverse('products:product-list')) 
    # create orderItem of the selected product
    order_item, status = OrderItem.objects.get_or_create(product=product)
    # create order associated with the user
    user_order, status = Order.objects.get_or_create(owner=user_profile, is_ordered=False)
    user_order.items.add(order_item)
    if status:
        # generate a reference code
        user_order.ref_code = generate_order_id()
        user_order.save()

    # show confirmation message and redirect back to the same page
    messages.info(request, "item added to cart")
    return redirect(reverse('products:product-list'))
