from django import forms
from django.forms import ModelForm
from .models import Servicio


class ServicioForm (ModelForm):

    class Meta:
        model = Servicio
        fields = [ 'nombre_servicio', 'valor_servicio', 'id_estado_servicio']
        


         