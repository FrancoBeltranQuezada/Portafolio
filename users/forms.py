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
        widgets ={
            'username':forms.TextInput(attrs={'class': 'form-control'}),
            'email':forms.EmailInput(attrs={'class': 'form-control','id':'materialLoginFormEmail'}),
            'first_name':forms.TextInput(attrs={'class': 'form-control'}),
            'last_name':forms.TextInput(attrs={'class': 'form-control'}),
            'rut':forms.TextInput(attrs={'class': 'form-control'}),
            'direccion':forms.TextInput(attrs={'class': 'form-control'}),
            'telefono':forms.TextInput(attrs={'class': 'form-control'}),
            'password1':forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2':forms.PasswordInput(attrs={'class': 'form-control'}),
        }


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

