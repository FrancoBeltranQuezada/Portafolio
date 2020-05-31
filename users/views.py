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












def UserUpdateProfile(request,pk):
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
            return redirect('user-list')
        else:
            print('no entro al if valid')
            
    else:
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = UserProfileForm(request.POST, instance=prof)

    return render(request, 'auth/user_form.html',{'user_form':user_form,'profile_form':profile_form})

    