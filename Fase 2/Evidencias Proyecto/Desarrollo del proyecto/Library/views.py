from django.shortcuts import render
from Library.models import *

# Create your views here.
def inicioBook(request):
    material =  MaterialBiblioteca.objects.all()
    instrumentos = Instrumento.objects.all()
    data = {'materiales' : material, "instrumentos" : instrumentos}


    return render(request,'iniciobiblioteca.html', data)


def detallebook(request,id):
    cosa = MaterialBiblioteca.objects.get(id_material  = id)


    data = {"material":cosa}

    return render(request, 'detallebiblioteca.html',data)