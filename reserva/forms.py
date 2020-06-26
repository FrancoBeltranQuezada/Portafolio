from django import forms
from .models import Reserva, Servicio, ModuloTiempo



class DateInputx(forms.DateInput):
    input_type = 'date'

class ReservaForm(forms.ModelForm):

    class Meta:
        model = Reserva
        fields = '__all__'
        widgets = {
            'patente': forms.TextInput(attrs={'class': 'form-control'}), 
            'marca':forms.TextInput(attrs={'class': 'form-control'}),
            'modelo':forms.TextInput(attrs={'class': 'form-control'}),
            'modulo_tiempo':forms.Select(attrs={'class': 'form-control'}),
            'servicio':forms.Select(attrs={'class': 'form-control'}),
            'fecha':forms.DateInput(attrs={'class': 'form-control  asd','id':'datepicker','placeholder':'Selected date'})
            
            }
