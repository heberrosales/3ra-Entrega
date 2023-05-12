from django.urls import path
from AppPortofino import views

urlpatterns = [
    #path('saludo/', views.saludo, name="saludo"),
    #path('fecha/', views.DiaDeHoy, name="fecha"),
    #path('nombre/<nombre>', views.MiNombre, name="nombre"),
    #path('plantilla/', views.pruebaPlantilla, name="plantilla"),
    path('', views.inicio, name="Inicio"),
    path('frutos-secos/', views.frutosSecos,name="frutossecos"),
    path('vinos/', views.vinos,name="vinos"),
    path('sucursales/', views.comentarios,name="sucursales"),
    path('sumar-vino/', views.sumar_vino, name="sumar_vino"),
    path('buscar-vino/', views.buscar_vinos, name="buscar_vinos")
]
