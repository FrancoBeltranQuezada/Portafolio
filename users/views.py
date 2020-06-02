from django.shortcuts import render, redirect,get_object_or_404
from django.contrib import messages
# form creado para que aparesca el email
from .forms import UserRegisterForm, UserProfileForm,UserUpdateForm,UserForm
from django.contrib.auth.forms import User
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import User, UserProfile
from django.urls import reverse_lazy
from django.forms import modelformset_factory
from django.http import HttpResponseRedirect
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from .mixin import GroupRequiredMixin
from django.contrib.auth.models import Group


# Create your views here.


def register(request):

    # si se envia un post request se valida la informacion, de no ser asi se carga el formulario vacio
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        profile_form = UserProfileForm(request.POST)
        if form.is_valid() and profile_form.is_valid():
            user = form.save()  # Se guarda el usuario creado en la BD
            #se define el grupo cliente como cliente
            cliente = Group.objects.get(name='cliente')
            #se le asigna el grupo cliente al usuario que se va a crear
            cliente.user_set.add(user)
            #se guarda el usuario con los datos de los campos del form y el grupo cliente
            user.save()
            
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            

            username = form.cleaned_data.get('username')
            # se envia mensaje de confirmacion y redirecciona
            messages.success(request, f'Acount created for {username}!')
            return redirect('login')
    else:
        form = UserRegisterForm()
        profile_form = UserProfileForm()

    return render(request, 'users/register.html', {'form': form, 'profile_form': profile_form})



def registrarEmpleado(request):

    # si se envia un post request se valida la informacion, de no ser asi se carga el formulario vacio
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        profile_form = UserProfileForm(request.POST)
        if form.is_valid() and profile_form.is_valid():
            user = form.save()  # Se guarda el usuario creado en la BD
            #se define el grupo cliente como empleado
            cliente = Group.objects.get(name='empleado')
            #se le asigna el grupo emplmeado al usuario que se va a crear
            cliente.user_set.add(user)
            #se guarda el usuario con los datos de los campos del form y el grupo cliente
            user.save()
            
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            

            username = form.cleaned_data.get('username')
            # se envia mensaje de confirmacion y redirecciona
            messages.success(request, f'Acount created for {username}!')
            return redirect('login')
    else:
        form = UserRegisterForm()
        profile_form = UserProfileForm()

    return render(request, 'empleados/registrar_empleado.html', {'form': form, 'profile_form': profile_form})


def listUser(request):
    context = {
        'usuarios': User.objects.all(),

    }
    return render(request, 'listar_user.html', context)

def homeview(request):
    return render(request,'users/home.html')


class EmpleadoListView(GroupRequiredMixin,ListView):
    group_required = [u'empleado', u'manager']
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
    template_name='empleados/empleado_confirm_delete.html'

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


class UserCreateView(CreateView):
    model = User
    fields = [
        'username',
        'email',
        'password1',
        'password2',
    ]
    # <app>/<model>_<viewtype>.html


# tipos de mensajes messages
# messages.debug
# messages.info
# messages.succes
# messages.warning
# messages.error

class UserDeleteView(DeleteView):
    model = User
    success_url = '/usuario/gestion-clientes/'


class UpdateUser(UpdateView):
    model = UserProfile
    second_model =  User
    template_name = 'auth/user_form.html'
    form_class = UserProfileForm
    second_form_class =  UserUpdateForm
    success_url = '/usuario/gestion-clientes/'

    def get_context_data(self, **kwargs):
        context = super(UpdateUser,self).get_context_data(**kwargs)
        pk = self.kwargs.get('pk',0)
        user = self.second_model.objects.get(id=pk)
        profile = self.model.objects.get(user_id=pk)
        if 'form' not in context:
            context['form'] = self.form_class(instance= profile)
        if 'form2' not in context:
            context['form2'] = self.second_form_class(instance =  user)
        context['id'] = pk
        return context
       
    def post(self,request, *args,**kwargs):
        self.object = self.get_object
        id_user = kwargs['pk']
        profile = self.model.objects.get(id=user_id)
        user = self.second_model.objects.get(id=id_user)
        form = self.form_class(request.POST, instance=user)
        form2 = self.second_form_class(request.POST, instance=profile)
        if form.is_valid() and form2.is_valid():
            form.save()
            form2.save()
            return HttpResponseRedirect(self.get_succes_url())
        else:
            return HttpResponseRedirect(self.get_succes_url())



def ErrorView(request):
    return render(request, 'base/error.html')

def EmpleadoUpdateProfile(request,pk):
    usr = User.objects.get(pk=pk)
    prof = UserProfile.objects.get(user_id=pk)
    print(usr.username)
   # print(usr.username)
    
    context={}
    
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=usr)   
        profile_form = UserProfileForm(request.POST, instance=prof)     
        #profile_form = UserProfileForm(instance=prof)
     #   users = User.objects.all().select_related('profile_form')
        
        if profile_form.is_valid() and user_form.is_valid():
            user_form.save()
            profile_form.save()
            print('si guardo')
            return redirect('empleado-list')
        else:
            print('no entro al if valid')
            
    else:
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = UserProfileForm(request.POST, instance=prof)

    return render(request, 'empleados/user_form.html',{'user_form':user_form,'profile_form':profile_form})






def UserUpdateProfile(request,pk):
    usr = User.objects.get(pk=pk)
    prof = UserProfile.objects.get(user_id=pk)
    print(usr.username)
    
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=usr)   
        profile_form = UserProfileForm(request.POST, instance=prof)     

        if profile_form.is_valid() and user_form.is_valid():
            user_form.save()
            profile_form.save()
            print('si guardo')
            return redirect('user-list')
        else:
            print('no entro al if valid')
            
    else:
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = UserProfileForm(request.POST, instance=prof)

    return render(request, 'auth/user_form.html',{'user_form':user_form,'profile_form':profile_form})

    