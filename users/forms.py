from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm

# se agregan nuevos campos al form de usuarios de django, para que se muestren en la vista de registro
# heredando el formulario de creacion de usaurios


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        # Este es el modelo con el que se relaciona
        model = User
        # Estos son los campos que queremos mostrar en nuestro formulario y en que orden
        fields = [
            'username',
            'email',
            'first_name',
            'last_name',
            'rut',
            'direccion',
            'telefono',
            'password1',
            'password2',
        ]


class UserUpdateForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        # Este es el modelo con el que se relaciona
        model = User
        # Estos son los campos que queremos mostrar en nuestro formulario y en que orden
        fields = [
            'username',
            'email',
            'first_name',
            'last_name',
            'rut',
            'direccion',
            'telefono',
        ]
     



class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email','rut',
            'direccion',
            'telefono')
        exclude = ['password1','password2','username']

