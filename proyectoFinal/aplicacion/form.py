from django import forms

class ClienteForm(forms.Form):
    nombre = forms.CharField(max_length=50, required=True)
    apellido = forms.CharField(required=True)
    email = forms.EmailField(label="Email", required=False)
    
class ProductoForm(forms.Form): 
    articulo = forms.CharField(max_length=50, )
    precio = forms.IntegerField()