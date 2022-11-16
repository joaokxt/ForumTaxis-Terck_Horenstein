from django.shortcuts import render
from django.http import HttpResponse
from .forms import *
from .models import *

# Create your views here.
def index(request):
    return render(request, 'inicio.html')

def mostrar_reservas(request):
    reservas = Reserva.objects.all()
    return render(request, 'reservas_mostrar.html', {'reservas':reservas})

def agregar_reservas(request):
    if request.method == 'POST':
        formulario = ReservaFormulario(request.POST)
        print(formulario)
        if formulario.is_valid() == True:
            informacion = formulario.cleaned_data
            reserva = Reserva(codigo=informacion['codigo'], nombre=informacion['nombre'], apellido=informacion['apellido'], email=informacion['email'], lugar=informacion['lugar'], vehiculo=informacion['vehiculo'])
            reserva.save()
            reservas = Reserva.objects.all()
            return render(request, 'reservas_mostrar.html', {'reservas':reservas})
    else:
        formulario=ReservaFormulario()
    return render(request, 'reservas_agregar.html', {"formulario":formulario})

def agregar_taxistas(request):
    if request.method == "POST":
        formulario = TaxistaFormulario(request.POST)
        if formulario.is_valid():
            datos = formulario.cleaned_data
            taxista = Taxista(nombre=datos["nombre"], apellido=datos["apellido"], telefono=datos["telefono"], email=datos["email"], matricula=datos["matricula"])
            taxista.save()
            taxistas = Taxista.objects.all()
            return render(request,"taxistas_mostrar.html", {"taxistas":taxistas})
    else:
        formulario = TaxistaFormulario()
    return render(request, "taxistas_agregar.html", {"formulario": formulario})

def mostrar_taxistas(request):
    taxistas = Taxista.objects.all()
    return render(request, "taxistas_mostrar.html", {"taxistas":taxistas})

def mostrar_vehiculos(request):
    vehiculos = Vehiculo.objects.all()
    return render(request, 'vehiculos_mostrar.html', {'vehiculos':vehiculos})

def agregar_vehiculos(request):
    if request.method == 'POST':
        formulario = VehiculoFormulario(request.POST)
        print(formulario)
        if formulario.is_valid() == True:
            informacion = formulario.cleaned_data
            vehiculo = Vehiculo(modelo=informacion['modelo'], patente=informacion['patente'], color=informacion['color'])
            vehiculo.save()
            vehiculos = Vehiculo.objects.all()
            return render(request, 'vehiculos_mostrar.html', {'vehiculos':vehiculos})
    else:
        formulario=VehiculoFormulario()
    return render(request, 'vehiculos_agregar.html', {"formulario":formulario})