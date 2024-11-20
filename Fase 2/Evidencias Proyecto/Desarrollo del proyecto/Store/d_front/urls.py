from django.urls import path
from .views import *

urlpatterns = [
    path('',                                        inicio,                                 name = "inicio"),
    path('buscar/<nombre>/',                        busqueda,                               name = "busqueda"),
    path('ordenes/',                                ordenes_usuario,                        name = "ordenes"),
    path("orden/creacion",                          crear_orden,                            name = "crearorden"),
    path('ordenes/detalle/<id>/',                   detalleorden,                           name = "detallesorden"),
    path('detalle/<id>/',                           detalle,                                name = "detalle"),
    path('carro/',                                  carro,                                  name = "carro"),
    path('AgregarProducto/<id>/',                   agregar_producto,                       name = "agregarProducto"),
    path('EliminarProducto/<id>/',                  eliminar_producto,                      name = "eliminarProducto"),
    path('RestarProducto/<id>/',                    restar_producto,                        name = "restarProducto"),
    path('LimpiarCarro/',                           vaciar_carro,                           name = "limpiarCarro"),
    path('orden/<int:id>/cambiar_estado/<int:nuevo_estado>/', cambiar_estado,               name = 'cambiar_estado'),
    path('orden/<int:id>/cancelar/',                cancelar_pedido,                        name = 'cancelar_pedido'),
    path('orden/<int:orden_id>/guardar_descripcion/', guardar_descripcion, name='guardar_descripcion'),
    path('perfil/', perfil_usuario, name='perfil_usuario'),


]

