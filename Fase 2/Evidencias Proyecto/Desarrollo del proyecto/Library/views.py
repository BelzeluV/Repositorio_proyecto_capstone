from django.http import Http404
from django.shortcuts import render
from Library.models import *
from Library.forms import *
from django.contrib import messages  # Para enviar mensajes de éxito o error
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from .models import MaterialBiblioteca, MensajeBiblioteca
from .forms import MensajeBibliotecaForm
# Create your views here.
def inicioBook(request):
    material =  MaterialBiblioteca.objects.all().order_by('nivel_aprendizaje')
    instrumentos = Instrumento.objects.all()
    data = {'materiales' : material, "instrumentos" : instrumentos}
    return render(request,'iniciobiblioteca.html', data)


def detallebook(request, id):
    # Obtenemos el material específico
    material = get_object_or_404(MaterialBiblioteca, id_material=id)
    mensajes = MensajeBiblioteca.objects.filter(material_asociado=material)

    # Procesamos el formulario de comentarios
    if request.method == 'POST':
        formulario = MensajeBibliotecaForm(request.POST)
        if formulario.is_valid():
            nuevo_mensaje = formulario.save(commit=False)
            nuevo_mensaje.material_asociado = material
            nuevo_mensaje.creado_por_usuario = request.user
            nuevo_mensaje.save()
            messages.success(request, "Comentario añadido exitosamente.")
            return redirect('bookdetalle', id=material.id_material)
        else:
            messages.error(request, "Hubo un error en el formulario. Intenta nuevamente.")
    else:
        formulario = MensajeBibliotecaForm()
    page = request.GET.get('page', 1)
    # Paginac   ión de los mensajes
    try:
        paginator = Paginator(mensajes, 3)
        mensajes = paginator.page(page)
    except:
        raise Http404# 'entity' contiene la página actual

    # Pasamos los datos al contexto
    data = {
        "material": material,
        "entity": mensajes,  # Comentarios paginados para el archivo paginator.html
        "paginator": paginator,  # Total de páginas para el archivo paginator.html
        "form": formulario,
    }

    return render(request, 'detallebiblioteca.html', data)
