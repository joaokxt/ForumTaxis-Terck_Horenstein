from django.db import models

# Create your models here.
class Reserva(models.Model):
    codigo = models.IntegerField()
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()    
    lugar = models.CharField(max_length=50)
    vehiculo = models.CharField(max_length=50)
    def __str__(self):
        return f"Código: {self.codigo} || Apellido y nombre: {self.apellido}, {self.nombre} || Email: {self.email} || Lugar: {self.lugar} || Vehículo: {self.vehiculo}"


class Taxista(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    telefono = models.IntegerField()
    email = models.EmailField()
    matricula = models.IntegerField()
    def __str__(self):
        return f"Matrícula: {self.matricula} || {self.nombre} {self.apellido} || E-mail: {self.email} || Telefono {self.telefono}"


class Vehiculo(models.Model):
    MODELOS = (
        ('Fiat Siena', 'Fiat Siena'),
        ('Fiat Cronos', 'Fiat Cronos'),
        ('Volkswagen Voyage', 'Volkswagen Voyage'),
        ('Chevrolet Corsa', 'Chevrolet Corsa')
    )
    COLORES = (
        ('Azul','Azul'),
        ('Negro', 'Negro'),
        ('Gris', 'Gris'),
    )
    modelo = models.CharField(max_length=50, choices=COLORES)
    patente = models.CharField(max_length=7)
    color = models.CharField(max_length=50, choices=MODELOS)
    def __str__(self):
        return f" {self.modelo} {self.color} || Patente: {self.patente}"

