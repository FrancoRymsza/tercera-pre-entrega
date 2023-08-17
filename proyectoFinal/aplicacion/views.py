from django.shortcuts import render
from django.http import HttpResponse

from .models import *
from .form import ClienteForm, ProductoForm
# Create your views here.

def home(request): 
    return render(request, "aplicacion/home.html")
    

def ingresarDatos(request): 
    if request.method == "POST" : 
      miForm = ClienteForm(request.POST)
      if miForm.is_valid(): 
        cliente_nombre = miForm.cleaned_data.get('nombre')
        cliente_apellido = miForm.cleaned_data.get('apellido')
        cliente = Cliente(nombre = cliente_nombre, 
                          apellido = cliente_apellido)
        
        cliente.save()
        return render(request, "aplicacion/home.html")

    else : 
        miForm = ClienteForm()
        
    return render(request, "aplicacion/ingresar_datos.html", {"form" : miForm})



def agregarProducto(request): 
    if request.method == "POST" : 
      miFormDos = ProductoForm(request.POST)
      if miFormDos.is_valid(): 
        articulo_nombre = miFormDos.cleaned_data.get('Nombre')
        articulo_precio = miFormDos.cleaned_data.get('Precio')
        variable = Producto(articulo = articulo_nombre, 
                            precio = articulo_precio)
        
        variable.save()
        return render(request, "aplicacion/home.html")
    
    else : 
        miFormDos = ProductoForm()  
    return render(request, "aplicacion/agregar_producto.html", {"miFormDos": miFormDos})


def buscar_datos(request):
    if request.GET.get['producto']:  # Obtener el término de búsqueda desde la URL
        query = request.GET['producto']
        items = Producto.objects.filter(nombre__icontains=query)  # Realizar búsqueda en la base de datos
    else:
        items = []

    context = {'producto': items, 'query': query}
    return render(request, 'buscar_datos.html', context)

def muestra_datos(request):
   context = {'Productos': Producto.objects.all() }
   return render(request, "aplicacion/muestra_datos.html")
   



        




    



    




