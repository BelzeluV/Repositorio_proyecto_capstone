from django.shortcuts import get_object_or_404, render,redirect
from Classes.models import *
from Classes.forms import *
from django.forms import modelformset_factory
# Create your views here.

from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

@login_required
def verificar_membresia(request):
    # Verificar si el usuario tiene una membresía activa
    usuario = request.user
    membresia = Membresia.objects.filter(usuario_asociado=usuario, activa=True).first()

    if membresia:
        # Redirigir a la página para usuarios con membresía activa
        return redirect('classinicio')  # Reemplaza 'pagina_membresia_activa' con el nombre de tu URL
    else:
        # Redirigir a la página para usuarios sin membresía activa
        return redirect('pagarmembresia')  # Reemplaza 'pagina_sin_membresia' con el nombre de tu URL


@login_required

def pagarmembresia(request):
    if request.method == "POST":
        usuario = request.user
        # Obtener el tipo de membresía (puedes ajustar la lógica para elegir el tipo)
        tipo_membresia = TipoMembresia.objects.first()  # Cambia esto si quieres un tipo específico
        if not tipo_membresia:
            return render(request, 'error.html', {'mensaje': 'No hay tipos de membresía definidos.'})
        
        # Crear una nueva membresía
        nueva_membresia = Membresia.objects.create(
            usuario_asociado=usuario,
            tipo_membresia=tipo_membresia,
            activa=True  # Puedes cambiar esta lógica según sea necesario
        )
        nueva_membresia.save()

        # Redirigir a una página después del registro
        return redirect('classinicio')  # Cambia esto a la URL de éxito

    # Renderizar el formulario
    return render(request, 'membresia\pagarmembresia.html')

@login_required

def classinicio(request):

    usuario = request.user
    membresia = Membresia.objects.filter

    asignaturaxalumno = AsignaturaXAlumno.objects.filter(id_alumno_usuario=usuario)
    asignaturas_alumno = Asignatura.objects.filter(id_asignatura__in=asignaturaxalumno.values_list('id_asignatura_rel', flat=True))
    data = {
        'asignaturasalumno' : asignaturas_alumno,
        'membresia': membresia
        }

    return render(request, 'clases/classinicio.html', data)

from django.db.models import Count, Q

@login_required
def classdetalle(request, id):
    asignatura = Asignatura.objects.get(id_asignatura=id)
    unidades = UnidadClase.objects.filter(materia_asociada=asignatura.id_asignatura).prefetch_related('contenidoclase_set')
    alumnos = AsignaturaXAlumno.objects.filter(id_asignatura_rel=asignatura)
    clases = Clase.objects.filter(asignatura=asignatura).order_by('-id_clase')
    form = ClaseForm()

    # Lógica para obtener registros de asistencia del usuario
    usuario = request.user
    try:
        asignatura_alumno = AsignaturaXAlumno.objects.get(id_asignatura_rel=asignatura, id_alumno_usuario=usuario)
        total_clases = clases.count()
        asistencias_confirmadas = Asistencia.objects.filter(
            asignatura_alumno=asignatura_alumno,
            confirmacion=True
        ).count()
        porcentaje_asistencia = (asistencias_confirmadas / total_clases) * 100 if total_clases > 0 else 0
    except AsignaturaXAlumno.DoesNotExist:
        asignatura_alumno = None
        total_clases = 0
        asistencias_confirmadas = 0
        porcentaje_asistencia = 0

    if request.method == 'POST':
        form = ClaseForm(request.POST)
        if form.is_valid():
            # Crear la clase sin asignatura, luego asignarla
            clase = form.save(commit=False)
            clase.asignatura = asignatura
            clase.save()

            # Crear asistencias para cada alumno inscrito en la asignatura
            for alumno in alumnos:
                Asistencia.objects.create(
                    clase_asistencia=clase,
                    asignatura_alumno=alumno,
                    confirmacion=False,
                    fecha_asistencia=clase.fecha_clase,
                )
            return redirect('detalleclase', id)
        else:
            print("Errores del formulario:", form.errors)

    data = {
        'a': asignatura,
        'unidades': unidades,
        'alumnos': alumnos,
        'clases': clases,
        'form': form,
        'asistencias_confirmadas': asistencias_confirmadas,
        'total_clases': total_clases,
        'porcentaje_asistencia': porcentaje_asistencia,
    }
    return render(request, 'clases/classdetalle.html', data)


@login_required

def detallecontenido(request, id):
    contenido = ContenidoClase.objects.get(id_contenido = id)
    data = {'contenido': contenido}
    return render(request, 'clases/detallecontenido.html',data)

@login_required

def verclase(request, id):
    clase = get_object_or_404(Clase, id_clase=id)
    form = ClaseForm(instance=clase)
    AsistenciaFormSet = modelformset_factory(Asistencia, form=AsistenciaForm, extra=0)
    asistencias = Asistencia.objects.filter(clase_asistencia=clase)
    formset = AsistenciaFormSet(queryset=asistencias)

    if request.method == 'POST':
        if 'btn-config' in request.POST:
            form = ClaseForm(request.POST, request.FILES, instance=clase)  # Asegúrate de incluir archivos
            print(form)
            if form.is_valid():
                form.save()
                return redirect('verclase', id=id)
            else:
                print("Errores del formulario de configuración:", form.errors)

        elif 'btn-asistencia' in request.POST:
            formset = AsistenciaFormSet(request.POST, queryset=asistencias)
            if formset.is_valid():
                for form in formset:
                    asistencia = form.save(commit=False)
                    asistencia.clase_asistencia = clase  # Asigna la clase correspondiente
                    asistencia.save()
                return redirect('verclase', id)

            else:
                for form in formset:
                    print("Errores en el formset:", form.errors)

    data = {'clase': clase, 'form': form, 'formset': formset}
    return render(request, 'clases/verclase.html', data)

