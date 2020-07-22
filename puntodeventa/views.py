from django.shortcuts import render, redirect
from .models import *
from servicio.models import Servicio
import json
import datetime
from django.http import JsonResponse
from proveedor.decorators import allowed_users
from django.views.generic import DeleteView,ListView
from .forms import CrearCustomerForm

# Create your views here.

@allowed_users(allowed_roles=['admin', 'empleado'])
def tienda(request):



    if request.user.is_authenticated:
        try:
            customer = request.user.customer
        except Customer.DoesNotExist:
            return render(request,'puntodeventa/error.html')
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_item': 0, 'shipping': False}
        cartItems = order['get_cart_items']

    products = Servicio.objects.all()

    context = {'products': products, 'cartItems': cartItems}

    return render(request, 'puntodeventa/tienda.html', context)


def carrito(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(
            customer=customer, complete=False)
        # se define la variable items, y se le asigna todos los items hijos de order, en este caso
        # orderitem, que son los productos anexados a la order
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_item': 0,'shipping':False}
        cartItems = order['get_cart_items']
    context = {'items': items, 'order': order,'cartItems':cartItems}

    return render(request, 'puntodeventa/carrito.html',context)

def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(
            customer=customer, complete=False)
        # se define la variable items, y se le asigna todos los items hijos de order, en este caso
        # orderitem, que son los productos anexados a la order
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total':0,'get_cart_item':0,'shipping':False}
        cartItems = order['get_cart_items']
    context = {'items':items,'order':order,'cartItems':cartItems}
    
    return render(request, 'puntodeventa/checkout.html',context)


def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action'] 

    print('Action:',action)
    print('productId:',productId)

    customer = request.user.customer
    product = Servicio.objects.get(id_servicio=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)

    orderItem,created = OrderItem.objects.get_or_create(order=order,product=product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action =='remove':
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('Item was added',safe=False)


def processOrder(request):
    # #se crea una id random para la transaccion con datos de la fecha/hora creada
    transaction_id = datetime.datetime.now().timestamp()
    # # parseo de los datos json
    data = json.loads(request.body)
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
    #     #aqui se pasa el total del json a la variable total
        total = float(data['form']['total'])
    #     #se asigna el id a la order
        order.transaction_id = transaction_id
    #     # si el total traido del json es igual al total del carrito entonces se completa la order y
    #     # se guarda en la bd
        if total == order.get_cart_total:
            order.complete = True
            print('precios distintos')
        order.save()
    # else:
    #     print('Not Logged')
    print('Data:',request.body)
    return JsonResponse('payment complete',safe=False)


def listarOrder(request):


    orders = Order.objects.all().order_by('-date_ordered')

    context = {'orders': orders}

    return render(request,'puntodeventa/ordenes.html',context)

class OrderDeleteView(DeleteView):
    model = Order
    template_name = 'puntodeventa/confirm_delete.html'
    success_url = '/listar_order/'

def crearCustomer (request):
    data = {
        'form': CrearCustomerForm()
    }

    if request.method == 'POST':
        formulario = CrearCustomerForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "Vendedor creado correctamente"
        else:
            data['mensaje'] = "El vendedor no se pudo guardar correctamente"


    return render (request,'puntodeventa/customer.html', data)

def ListarCustomer(request):
    customers = Customer.objects.all()
    context = {
        'customers':customers
    }
    return render(request,'puntodeventa/listar_customer.html',context)

class EliminarCustomer(DeleteView):
    model= Customer
    template_name = 'puntodeventa/eliminar_customer.html'
    success_url ='/'