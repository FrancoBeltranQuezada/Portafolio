from django.shortcuts import render,redirect
from django.contrib import messages
#form creado para que aparesca el email
from .forms import UserRegisterForm

# Create your views here.
def register(request):

    #si se envia un post request se valida la informacion, de no ser asi se carga el formulario vacio
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()#Se guarda el usuario creado en la BD
            username = form.cleaned_data.get('username')
            #se envia mensaje de confirmacion y redirecciona
            messages.success(request, f'Acount created for {username}!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    
   
    return render(request,'users/register.html',{'form':form})


#tipos de mensajes messages
#messages.debug
#messages.info
#messages.succes
#messages.warning
#messages.error