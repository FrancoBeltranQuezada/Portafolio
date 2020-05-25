from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile

# se agregan nuevos campos al form de usuarios de django, para que se muestren en la vista de registro
# heredando el formulario de creacion de usaurios
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        #Este es el modelo con el que se relaciona
        model = User
        #Estos son los campos que queremos mostrar en nuestro formulario y en que orden
        fields = [
            'username',
            'email',
            'password1',
            'password2',
        ]

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields=('direccion','telefono','rut')