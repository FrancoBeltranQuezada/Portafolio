from django import forms
from .models import prov

class ProvForm(forms.ModelForm):
    class Meta:
        model = prov
        fields = '__all__'