import random
from django.shortcuts import render,redirect
from Store.Cart import Carrito  
from Store.models import *
from django.contrib import messages



# Create your views here.
def inicio(request):
    productos = Producto.objects.all()
    data = {"productos": productos}
    return render(request, "frontoffice/inicio/inicio.html", data)


def detalle(request,id):
    #despliegue 
    lista_productos   = Producto.objects.all()
    producto          = Producto.objects.get(id)
    marca             = Marca.objects.get(producto.marca)
    subcategoria      = Subcategoria.objects.get(producto.subcat_producto)
    categoria         = Categoria.objects.get(producto.categoria_producto)
    tipoprod          = TipoProducto.objects.get(producto.tipo_producto)
    lista_random      = random.sample(list(lista_productos),3)
    
    print("producto:"+str(producto)+"\nmarca: "+str(marca)+"\nsubcategoria: "+str(subcategoria)+"\ncategoria: "+str(categoria)+"\ntipoprod"+str(tipoprod))
    #manejo de la pagina
    data = {"producto" : producto, "recomendaciones" : lista_random, "marca" : marca, "subcategoria" : subcategoria,"categoria" : categoria, "tipo": tipoprod}
    return render(request, "frontoffice/detalles/detalle.html", data)




def carro(request):
    return render(request, "frontoffice/carro/carro.html")

def agregar_producto(request,id):
    carro = Carrito.Carro(request)
    producto = Producto.objects.get(id_producto = id)
    carro.agregar(Producto = producto) 
    messages.success(request,"Producto agregado con éxito")
    return redirect(to="carro")

def eliminar_producto(request,id):
    carro = Carrito.Carro(request)
    producto = Producto.objects.get(id_producto = id)
    carro.eliminar(Producto = producto)
    messages.success(request,"Producto eliminado con éxito")
    return redirect(to="carro")

def restar_producto(request,id):
    carro = Carrito.Carro(request)
    producto = Producto.objects.get(id_producto = id)
    carro.restar_producto(Producto = producto)
    return redirect(to="carro")

def vaciar_carro(request):
    carro = Carrito.Carro(request)
    carro.limpiar_carro()
    messages.success(request,"El carro fue Vaciado")
    return redirect("")