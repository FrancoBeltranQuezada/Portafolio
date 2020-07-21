from django import forms
from .models import Customer


class CrearCustomerForm(forms.ModelForm):
    class Meta:
        # Este es el modelo con el que se relaciona
        model = Customer
        # Estos son los campos que queremos mostrar en nuestro formulario y en que orden
        fields = [
        'user',

        ]       
        exclude = ['name','email']


