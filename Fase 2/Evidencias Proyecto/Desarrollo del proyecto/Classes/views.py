from django.shortcuts import render,redirect
from Classes.models import *
from Classes.forms import *
# Create your views here.
def classinicio2(request):
    usuario = request.user
    asignaturaxalumno = AsignaturaXAlumno.objects.filter(id_alumno_usuario=usuario)
    asignatura = Asignatura.objects.filter(id_asignatura__in=asignaturaxalumno.values_list('id_asignatura_rel', flat=True))



    data = {}
    return render(request, 'clases/classinicio.html',data)


def classinicio(request):

    usuario = request.user
    asignaturaxalumno = AsignaturaXAlumno.objects.filter(id_alumno_usuario=usuario)
    asignaturas_alumno = Asignatura.objects.filter(id_asignatura__in=asignaturaxalumno.values_list('id_asignatura_rel', flat=True))
    data = {'asignaturasalumno' : asignaturas_alumno}

    return render(request, 'clases/classinicio.html', data)

def classdetalle(request, id):
    asignatura = Asignatura.objects.get(id_asignatura=id)
    unidades = UnidadClase.objects.filter(materia_asociada=asignatura.id_asignatura).prefetch_related('contenidoclase_set')
    alumnos = AsignaturaXAlumno.objects.filter(id_asignatura_rel=asignatura)
    clases = Clase.objects.filter(asignatura=asignatura)
    form = ClaseForm()

    if request.method == 'POST':
        form = ClaseForm(request.POST)
        print(form)
        if form.is_valid():
            # Crear la clase sin asignatura, luego asignarla
            clase = form.save(commit=False)
            clase.asignatura = asignatura  # Asignar la asignatura cargada en la vista
            print(clase)
            clase.save()

            # Obtener todos los alumnos inscritos en la asignatura
            alumnos_inscritos = AsignaturaXAlumno.objects.filter(
                id_asignatura_rel=asignatura
            )

            # Crear asistencias para cada alumno
            for alumno in alumnos_inscritos:
                Asistencia.objects.create(
                    clase_asistencia=clase,
                    asignatura_alumno=alumno,
                    confirmacion=False,  # Por defecto no confirmada
                    fecha_asistencia=clase.fecha_clase,
                )
            return redirect('detalleclase',id)  # Redirigir a una lista de clases o página deseada
        else:
            print("Errores del formulario:", form.errors)  # Imprime errores en la consola

    data = {
        'a': asignatura,
        'unidades': unidades,
        'alumnos': alumnos,
        'clases': clases,
        'form': form
    }
    return render(request, 'clases/classdetalle.html', data)

def detallecontenido(request, id):
    contenido = ContenidoClase.objects.get(id_contenido = id)
    data = {'contenido': contenido}
    return render(request, 'clases/detallecontenido.html',data)


def pagarmembresia(request):
    data = {}
    return render(request, 'membresia\pagarmembresia.html', data)

def consultarmembresia(request):
    usuario = request.user
    membresia = Membresia.objects.filter()
    return render()

def verclase(request,id):
    clase = Clase.objects.get(id_clase= id)
    


    return render(request,'clases/verclase.html', {'clase':clase}) 