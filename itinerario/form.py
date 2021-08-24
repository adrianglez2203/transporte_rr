from django.forms import ModelForm
from django import forms
from itinerario.models import Viaje, Trabajador, Taxi

class TaxiForm(ModelForm):
    class Meta:
        model = Taxi
        fields = '__all__'
        # widgets = {
        #     'chofer': forms.CharField(),
        #     'capacidad':forms.NumberInput(),
        #     'nombre':forms.CharField(),
        #     'telefono':forms.CharField(),
        #     'tipo':forms.CharField(),
        # }
class TrabajadorForm(ModelForm):
    class Meta:
        model = Trabajador
        fields = '__all__'
class ViajeForm(ModelForm):
    class Meta:
        model = Viaje
        fields = '__all__'