from django import forms
from .models import Vehiculo

class ReservaFormulario(forms.Form):
    codigo = forms.IntegerField()
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    email = forms.EmailField()    
    lugar = forms.CharField(max_length=50)
    vehiculo = forms.CharField(max_length=50)

class VehiculoFormulario(forms.Form):
    modelo = forms.ChoiceField(choices=Vehiculo.MODELOS)
    patente = forms.CharField(max_length=7)
    color = forms.ChoiceField(choices=Vehiculo.COLORES)

class TaxistaFormulario(forms.Form):
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    telefono = forms.IntegerField()
    email = forms.EmailField()
    matricula = forms.IntegerField()