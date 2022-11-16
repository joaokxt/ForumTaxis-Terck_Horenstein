from django.urls import path
from AppTaxi import views

urlpatterns = [
    path('reservas/', views.mostrar_reservas, name='reservas_mostrar'),
    path('reservas_agregar/', views.agregar_reservas, name='reservas_agregar'),
    path('vehiculos/', views.mostrar_vehiculos, name='vehiculos_mostrar'),
    path('vehiculos_agregar/', views.agregar_vehiculos, name='vehiculos_agregar'),
    path('taxistas/', views.mostrar_taxistas, name='taxistas_mostrar'),
    path('taxistas_agregar/', views.agregar_taxistas, name='taxistas_agregar'),
]