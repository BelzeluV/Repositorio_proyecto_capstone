
from django.conf import settings
from django.urls import path
from Classes.views import *

urlpatterns = [
#partes vitales del proyecto
    path('inicio/',  classinicio,  name='classinicio'),
    path('detalle/<id>', classdetalle, name="detalleclase"),
    path('detalle/contenido/<id>', detallecontenido, name="contenidodetalle"),
    path('clase/ver/<id>' ,verclase,   name='verclase'),

    path('membresia/consultar/<id>', consultarmembresia, name='consultarmembresia'),
    path('pagar/Membresia', pagarmembresia, name="pagarmembresia"),
]