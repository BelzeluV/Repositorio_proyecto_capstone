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
]