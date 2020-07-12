from django import forms
from .models import Boleta, DetalleBoleta, Servicio
from betterforms.multiform import MultiModelForm
from datetime import datetime


class DetalleBoletaForm(forms.ModelForm):
    
    class Meta :
        model = DetalleBoleta
        fields = '__all__'
        widgets = {
            'servicio': forms.Select(attrs={'class': 'form-control select2'}),
            'desc_prod': forms.Textarea(attrs={'class':'form-control'}),
            'cantidad': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese cantidad'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control'})
            
        }


class BoletaForm (forms.ModelForm):
    
    class Meta:
        model = Boleta
        fields = '__all__'
        widgets = {
            'fecha':forms.DateInput(attrs={'class': 'form-control  asd','id':'datepicker','placeholder':'Selected date','autocomplete':'off'}),
            'usuario': forms.Select(attrs = {'class': 'form-control select2'}),
            'total': forms.NumberInput(attrs={'class': 'form-control', 'readonly': True})
        }






class BoletaMultiForm(MultiModelForm):
    form_classes = {
        'boleta': BoletaForm,
        'detalleBoleta': DetalleBoletaForm,
    }
        

