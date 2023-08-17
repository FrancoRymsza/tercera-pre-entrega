from django.db import models

# Create your models here.

class Cliente(models.Model): 
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nombre , self.apellido}"
    
class Producto(models.Model):
    articulo = models.CharField(max_length=50, null=True )
    precio = models.IntegerField(null=True)

    def __str__(self): 
        return f"{self.articulo, self.precio}"
    
    

                  
    
