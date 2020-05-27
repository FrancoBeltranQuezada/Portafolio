from django.shortcuts import render, redirect
from django.contrib import messages
# form creado para que aparesca el email
from .forms import UserRegisterForm, UserProfileForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView,DeleteView
from .models import User, UserProfile
from django.urls import reverse_lazy

# Create your views here.


def register(request):

    # si se envia un post request se valida la informacion, de no ser asi se carga el formulario vacio
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        profile_form = UserProfileForm(request.POST)
        if form.is_valid() and profile_form.is_valid():
            user = form.save()  # Se guarda el usuario creado en la BD
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


def listUser(request):
    context = {
        'usuarios': User.objects.all(),

    }
    return render(request, 'listar_user.html', context)


class UserListView(ListView):
    model = User
    template_name = 'users/listar_user.html'
    context_object_name = 'usuarios'
    ordering = ['-date_joined']


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


class UserUpdateView(UpdateView):
    model = User
    fields = [
        'username',
        'first_name',
        'last_name',
        'email',
        
    ]


# tipos de mensajes messages
# messages.debug
# messages.info
# messages.succes
# messages.warning
# messages.error

class UserDeleteView(DeleteView):
    model = User
    success_url= '/usuario/gestion-clientes/'
    
    


