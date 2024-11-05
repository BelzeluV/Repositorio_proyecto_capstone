from django.shortcuts import render
from Library.models import *

# Create your views here.
def inicioBook(request):
    material =  MaterialBiblioteca.objects.all()
    instrumentos = Instrumento.objects.all()
    data = {'materiales' : material, "instrumentos" : instrumentos}


    return render(request,'iniciobiblioteca.html', data)

def detallebook(request, id):
    material = MaterialBiblioteca.objects.get(id_material=id)
    mensajes = MensajeBiblioteca.objects.filter(material_asociado=material)

    data = {"material": material, "mensajes": mensajes}

    return render(request, 'detallebiblioteca.html', data)
