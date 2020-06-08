from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
# form creado para que aparesca el email
from .forms import UserRegisterForm, UserForm, UserUpdateForm

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.forms import modelformset_factory
from django.http import HttpResponseRedirect
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from .mixin import GroupRequiredMixin
from django.contrib.auth.models import Group
from .models import User

# Create your views here.


def homeview(request):
    username = None
    if request.user.is_authenticated:
        username = request.user.first_name
    return render(request, 'users/home.html',{'username':username})


def ErrorView(request):
    return render(request, 'base/error.html')


def register(request):
    # si se envia un post request se valida la informacion, de no ser asi se carga el formulario vacio
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()  # Se guarda el usuario creado en la BD
            # se define el grupo cliente como cliente
            cliente = Group.objects.get(name='cliente')
            # se le asigna el grupo cliente al usuario que se va a crear
            cliente.user_set.add(user)
            # se guarda el usuario con los datos de los campos del form y el grupo cliente
            user.save()
            username = form.cleaned_data.get('username')
            # se envia mensaje de confirmacion y redirecciona
            messages.success(request, f'Acount created for {username}!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


class UserListView(GroupRequiredMixin,ListView):
    group_required = [u'empleado', u'manager']
    model = User
    template_name = 'users/listar_user.html'
    context_object_name = 'usuarios'
    ordering = ['-date_joined']

    def get_queryset(self):

        return User.objects.filter(groups='1')


class UserDetailView(DetailView):
    model = User
    # <app>/<model>_<viewtype>.html


class UserDeleteView(DeleteView):
    model = User
    success_url = '/usuario/gestion-clientes/'


def UpdateUserView(request, pk):
    user = User.objects.get(pk=pk)

    if request.method == 'POST':
        form = UserForm(data=request.POST, instance=user)
        if form.is_valid():
            form.save()
            print('si guardpo')
            return redirect('user-list')
        else:
            print('no guardó')
    else:
        form = UserForm(instance=user)
    return render(request, 'users/user_form.html', {'form': form})


def registrarEmpleado(request):
    # si se envia un post request se valida la informacion, de no ser asi se carga el formulario vacio
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()  # Se guarda el usuario creado en la BD
            # se define el grupo empleado como empleado
            empleado = Group.objects.get(name='empleado')
            # se le asigna el grupo cliente al usuario que se va a crear
            empleado.user_set.add(user)
            # se guarda el usuario con los datos de los campos del form y el grupo empleado
            user.save()
            username = form.cleaned_data.get('username')
            # se envia mensaje de confirmacion y redirecciona
            messages.success(request, f'Acount created for {username}!')
            return redirect('empleado-list')
    else:
        form = UserRegisterForm()
    return render(request, 'empleados/registrar_empleado.html', {'form': form})


class EmpleadoListView(ListView):

    model = User
    template_name = 'empleados/listar_empleado.html'
    context_object_name = 'usuarios'
    ordering = ['-date_joined']

    def get_queryset(self):

        return User.objects.filter(groups='2')


class EmpleadoDetailView(DetailView):
    model = User
    # <app>/<model>_<viewtype>.html


class EmpleadoDeleteView(DeleteView):
    model = User
    success_url = '/usuario/gestion-empleado/'
    template_name = 'empleados/empleado_confirm_delete.html'


def UpdateEmpleadoView(request, pk):
    user = User.objects.get(pk=pk)

    if request.method == 'POST':
        form = UserForm(data=request.POST, instance=user)
        if form.is_valid():
            form.save()
            print('si guardpo')
            return redirect('empleado-list')
        else:
            print('no guardó')
    else:
        form = UserForm(instance=user)
    return render(request, 'users/user_form.html', {'form': form})
