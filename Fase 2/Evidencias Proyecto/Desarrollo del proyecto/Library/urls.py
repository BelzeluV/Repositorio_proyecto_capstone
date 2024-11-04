
from django.conf import settings
from django.urls import path
from Library.views import *

urlpatterns = [
#partes vitales del proyecto
    path('inicio/',     inicioBook,  name='bookinicio'),
    path('detalles/<id>/',   detallebook, name= 'bookdetalle')
]