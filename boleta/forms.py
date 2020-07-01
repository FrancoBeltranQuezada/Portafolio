from django import forms
from .models import Boleta, DetalleBoleta, Servicio
from betterforms.multiform import MultiModelForm
from datetime import datetime


class DetalleBoletaForm(forms.ModelForm):
    
    class Meta :
        model = DetalleBoleta
        fields = '__all__'
        widgets = {
            'servicio': forms.Select(attrs={'class': 'form-control'}),
            'desc_prod': forms.NumberInput(attrs={'class':'form-control', 'placeholder': 'Ingrese descuento'}),
            'cantidad': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese cantidad'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control'})
            
        }


class BoletaForm (forms.ModelForm):
    
    class Meta:
        model = Boleta
        fields = '__all__'
        widgets = {
            'fecha':forms.DateInput(format = '%Y-%m-%d', attrs={'class': 'form-control', 'value': datetime.now().strftime('%Y-%m-%d')}),
            'usuario': forms.Select(attrs = {'class': 'form-control'}),
            'total': forms.NumberInput(attrs={'class': 'form-control'})
        }









class BoletaMultiForm(MultiModelForm):
    form_classes = {
        'boleta': BoletaForm,
        'detalleBoleta': DetalleBoletaForm,
    }
        

