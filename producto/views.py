from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Producto, EstadoProducto
from .forms import ProductoForm

# Create your views here.

def home (request):
    productos = Producto.objects.all()
    contexto ={
        'productos':productos
    }
    return render(request,'producto/index.html',contexto)


def about (request):
    return render(request,'producto/about.html')


def crear_producto(request):
    contexto ={
        'form': ProductoForm
    }
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            contexto['mensaje'] = "Guardado correctamente"
        return redirect('producto-home')

    return render(request, 'producto/crear_producto.html',contexto)

    
def editar_producto(request, id_producto):
    productos = Producto.objects.get(id_producto=id_producto)
    if request.method == 'GET':
        form = ProductoForm(instance=productos)
        context = {
            'form':form
        }
    else:
        form = ProductoForm(request.POST, instance = productos)
        context = {
            'form':form
        }
        if form.is_valid():
            form.save()
            return redirect('producto-home')
    return render(request,'producto/crear_producto.html',context)


def eliminar_producto(request, id_producto):
    productos = Producto.objects.get(id_producto=id_producto)

    if request.method == 'POST':
        productos.delete()
        return redirect('producto-home')
    return render(request, 'producto/eliminar.html',{'productos':productos})





