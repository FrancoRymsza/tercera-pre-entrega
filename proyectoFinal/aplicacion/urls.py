from django.urls import path 
from .views import * 

urlpatterns = [
    path('', home , name = "home" ),
    
    path('ingresar_datos/', ingresarDatos, name = 'ingresar_datos'),
    path('agregar_producto/', agregarProducto, name = 'agregar_producto'),

    path('buscar_datos/', buscar_datos, name = 'buscar_datos'),
    path('muestra_datos/', muestra_datos, name = 'muestra_datos'),
    

    
    
]
