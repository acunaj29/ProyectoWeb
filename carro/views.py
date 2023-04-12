from django.shortcuts import render,redirect
from .carro import Carro
from tienda.models import Producto
# Create your views here.

def agregar_producto(request, producto_id):
    carro=carro(request)
    Producto=Producto.objects.get(id=producto_id)

    Carro.Agregar(Producto=Producto)

    return redirect("tienda")

def eliminar_producto(request, producto_id):
    carro=carro(request)
    Producto=Producto.objects.get(id=producto_id)

    Carro.eliminar(Producto=Producto)

    return redirect("tienda")

def restar_producto(request, producto_id):
    carro=carro(request)
    Producto=Producto.objects.get(id=producto_id)

    Carro.restar_producto(Producto=Producto)

    return redirect("tienda")

def limpiar_carro(request, producto_id):
    carro=carro(request)
    Carro.limpiar_carro()

    return redirect("tienda")