
# Create your views here.
# app_productos/views.py

from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto

# Listar productos (READ)
def listar_productos(request):
    productos = Producto.objects.all()
    return render(request, 'listar_productos.html', {'productos': productos})

# Agregar producto (CREATE)
def agregar_producto(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        categoria = request.POST['categoria']
        precio = request.POST['precio']
        descripcion = request.POST.get('descripcion', '')
        existencias = request.POST.get('existencias', 0)

        Producto.objects.create(
            nombre=nombre,
            categoria=categoria,
            precio=precio,
            descripcion=descripcion,
            existencias=existencias
        )
        return redirect('listar_productos')
    return render(request, 'agregar_producto.html')

# Editar producto (UPDATE)
def editar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        producto.nombre = request.POST['nombre']
        producto.categoria = request.POST['categoria']
        producto.precio = request.POST['precio']
        producto.descripcion = request.POST.get('descripcion', '')
        producto.existencias = request.POST.get('existencias', 0)
        producto.save()
        return redirect('listar_productos')
    return render(request, 'editar_producto.html', {'producto': producto})

# Borrar producto (DELETE)
def borrar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        producto.delete()
        return redirect('listar_productos')
    return render(request, 'borrar_producto.html', {'producto': producto})