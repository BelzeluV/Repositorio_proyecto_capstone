import random
from django.http import Http404
from django.shortcuts import get_object_or_404, render,redirect
from Store.Cart import Carrito  
from Store.models import *
from django.contrib import messages
from Store.forms import  *
from django.core.paginator import Paginator
from django.urls import reverse


# Create your views here.
def inicio(request):
    productos   = Producto.objects.all()
    data = {"productos": productos}

    return render(request, "frontoffice/inicio/inicio.html", data)

def busqueda(request, nombre):
    print(nombre)
    productos = Producto.objects.filter(nombre_producto__icontains =nombre)
    print(productos)
    data = {"entity": productos}
    return render(request, "frontoffice/busqueda/busqueda.html", data)

def detalle(request,id):
    #despliegue 
    print(id)
    lista_productos   = Producto.objects.all()
    producto          = Producto.objects.get(id_producto =  id)
    marca             = Marca.objects.get(id_marca = producto.marca.id_marca)
    subcategoria      = Subcategoria.objects.get(id_subcategoria = producto.subcat_producto.id_subcategoria)
    categoria         = Categoria.objects.get(id_categoria = producto.categoria_producto.id_categoria)
    tipoprod          = TipoProducto.objects.get(id_tipo =producto.tipo_producto.id_tipo)
    lista_random      = random.sample(list(lista_productos),3)
    
    print("producto:"+str(producto)+"\nmarca: "+str(marca)+"\nsubcategoria: "+str(subcategoria)+"\ncategoria: "+str(categoria)+"\ntipoprod"+str(tipoprod))
    #manejo de la pagina
    data = {"producto" : producto, "recomendaciones" : lista_random, "marca" : marca, "subcategoria" : subcategoria,"categoria" : categoria, "tipo": tipoprod}
    return render(request, "frontoffice/detalles/detalle.html", data)


def carro(request):
    formulario = OrdenForm

    data = {"formulario": formulario}
    if request.method == 'POST':
        formulario = OrdenForm(request.POST)
        if formulario.is_valid():
            carro = Carro(request)  # Obtener el carro actual

            # Calcular el total del pedido
            total = sum(item['precio'] * item['cantidad'] for item in carro.carro.values())

            # Crear una nueva orden
            nueva_orden = Orden.objects.create(
                descripcion=formulario.cleaned_data['descripcion'],
                nombre_quien_recibe=formulario.cleaned_data['nombre_quien_recibe'],
                direccion_entrega=formulario.cleaned_data['direccion_entrega'],
                estado=0,  # Estado inicial
                usuario_rel=request.user,
                total=total
            )

            for item in carro.carro.values():
                producto = Producto.objects.get(id_producto=item['id_producto'])
                Ordenxproducto.objects.create(
                    id_orden_relacion=nueva_orden,
                    id_producto=producto,
                    valorado=False,
                    cantidad_producto=item['cantidad'],
                    cantidad_estrellas=0
                )

            carro.limpiar_carro()


    return render(request, "frontoffice/carro/carro.html",data)

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


"""
#funcion original para las ordenes del usuario
def ordenes_usuario(request):
    # Filtra las órdenes por el usuario actual
    # Filtra las órdenes por el usuario actual
    ordenes = Orden.objects.filter(usuario_rel=request.user)
    page = request.GET.get('page', 1)

    # Obtén todos los productos relacionados con las órdenes de ese usuario
    ordenxproductos = Ordenxproducto.objects.filter(id_orden_relacion__in=ordenes)
    productos = Producto.objects.filter(id_producto__in=ordenxproductos.values_list('id_producto', flat=True))

    try:
        paginator = Paginator(ordenes, 4)
        ordenes = paginator.page(page)
    except:
        raise Http404

    data = {'entity': ordenes, 'paginator': paginator, 'ordenxproductos': ordenxproductos, 'productos': productos}
    return render(request, 'frontoffice/orden/listaordenes.html', data)
"""


def ordenes_usuario(request):
    ordenes = Orden.objects.filter(usuario_rel=request.user)
    
    # Filter by order status
    estado = request.GET.get('estado')
    if estado:
        ordenes = ordenes.filter(estado=estado)

    # Filter by creation date range
    fecha_inicio = request.GET.get('fecha_inicio')
    fecha_fin = request.GET.get('fecha_fin')
    if fecha_inicio and fecha_fin:
        ordenes = ordenes.filter(fecha_creacion__range=[fecha_inicio, fecha_fin])

    # Filter by recipient name
    recipient_name = request.GET.get('nombre_recibe')
    if recipient_name:
        ordenes = ordenes.filter(nombre_quien_recibe__icontains=recipient_name)
    
    # Filter by product in order
    producto_id = request.GET.get('producto_id')
    if producto_id:
        orden_ids = Ordenxproducto.objects.filter(id_producto_id=producto_id, id_orden_relacion__usuario_rel=request.user).values_list('id_orden_relacion', flat=True)
        ordenes = ordenes.filter(id_orden__in=orden_ids)

    # Pagination and context setup
    page = request.GET.get('page', 1)
    try:
        paginator = Paginator(ordenes, 4)
        ordenes = paginator.page(page)
    except:
        raise Http404

    data = {
        'entity': ordenes,
        'paginator': paginator,
        'ordenxproductos': Ordenxproducto.objects.filter(id_orden_relacion__in=ordenes),
        'productos': Producto.objects.filter(id_producto__in=Ordenxproducto.objects.values_list('id_producto', flat=True)),
        'opcionEstado': opcionEstado  # Pass status options for filter dropdown
    }
    return render(request, 'frontoffice/orden/listaordenes.html', data)


from Store.Cart.Carrito import Carro

def crear_orden(request):
    direccion  =  0
    
    carro = Carro(request)  # Obtener el carro actual
    total = sum(item['precio'] * item['cantidad'] for item in carro.carro.values())  # Calcular el total del pedido

    # Crear una nueva orden
    nueva_orden = Orden.objects.create(
        descripcion=f'Orden para {request.user.username}',
        nombre_quien_recibe=request.user.username,  # Esto puede cambiarse si tienes un campo para ingresar el nombre del receptor
        direccion_entrega= direccion,  # Puedes usar un formulario para obtener la dirección real
        estado=0,  # Estado inicial
        usuario_rel=request.user,
        total=total
    )
    for item in carro.carro.values():
        producto = Producto.objects.get(id_producto=item['id_producto'])
        Ordenxproducto.objects.create(
            id_orden_relacion=nueva_orden,
            id_producto=producto,
            valorado=False,  # Se marcará como "valorado" después
            cantidad_producto=item['cantidad'],
            cantidad_estrellas = 0
        )
    carro.limpiar_carro()
    return redirect('detallesorden', id = nueva_orden.id_orden)

def detalleorden(request, id):
    opcionEstado = [
    [0,"empacando"],
    [1,"esperando viaje"],
    [2,"enviado"],
    [3,"entregado"],
    [4,"cancelado"]]  
    # Obtener la orden específica por su ID
    orden = get_object_or_404(Orden, id_orden=id)
    
    # Filtrar todos los registros en Ordenxproducto relacionados a esta orden
    ordenxproductos = Ordenxproducto.objects.filter(id_orden_relacion=orden.id_orden)
    
    # Obtener los productos relacionados con la orden
    productos = Producto.objects.filter(id_producto__in=ordenxproductos.values('id_producto'))
    page = request.GET.get('page', 1)

    infotabla = ''  # Si necesitas más información para la tabla, puedes agregarla aquí
    try:
        paginator = Paginator(productos, 4)
        productos = paginator.page(page)
    except:
        raise Http404
    # Pasar los datos al template
    data = {
        "orden": orden,
        "entity": productos,
        "ordenxproducto": ordenxproductos,
        "informacion": infotabla,
        'paginator': paginator,
        "opcionEstado":opcionEstado
    }
    
    return render(request, "frontoffice/orden/detalleorden.html", data)

from django.shortcuts import redirect

def cambiar_estado(request, id, nuevo_estado):
    orden = get_object_or_404(Orden, id_orden=id)
    orden.estado = nuevo_estado
    orden.save()
    return redirect('detallesorden', id=id)

def cancelar_pedido(request, id):
    orden = get_object_or_404(Orden, id_orden=id)
    if orden.estado in [0, 1]:  # Solo cancelar si está en empacado o esperando viaje
        orden.estado = 4  # Estado "Cancelado"
        orden.save()
    return redirect('detallesorden', id=id)

def guardar_descripcion(request, orden_id):
    # Verificamos que la solicitud sea POST
    if request.method == 'POST':
        orden = get_object_or_404(Orden, id_orden=orden_id)
        
        # Actualizamos la descripción solo si el campo está en el formulario
        nueva_descripcion = request.POST.get('descripcion')
        if nueva_descripcion is not None:
            orden.descripcion = nueva_descripcion
            orden.save()  # Guardamos la orden con la descripción actualizada
        
        # Redirigimos a la misma página o a una página específica después de guardar
        return redirect(reverse('detallesorden', args=[orden_id]))  # Asegúrate de tener esta vista o usa la que necesitas
    else:
        # Si la solicitud no es POST, redirigimos a la página de detalles de la orden o a la principal
        return redirect(reverse('detallesorden', args=[orden_id]))
