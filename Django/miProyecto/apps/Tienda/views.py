from django.shortcuts import render
from .models import *

# Create your views here.

def cargarInicio(request):
    productos = Producto.objects.all()
    cate_perros = Producto.objects.filter(categoria_id = 1)
    cate_gatos = Producto.objects.filter(categoria_id = 2)
    return render(request, "inicio.html",{"prod":productos, "cate_perro": cate_perros, "cate_gato": cate_gatos})

def cargarAgregarProducto(request):
    categorias = Categoria.objects.all()
    return render(request,"agregarProducto.html",{"cate": categorias})