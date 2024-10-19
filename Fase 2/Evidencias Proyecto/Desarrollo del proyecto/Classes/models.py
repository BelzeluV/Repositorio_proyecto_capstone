from django.db import models
from Store.models import Usuario
from django_quill.fields import QuillField
from django.core.exceptions import ValidationError


# Create your models here.

class TipoMembresia(models.Model):
    id_tipo_membresia   = models.AutoField(primary_key = True)
    nombre_membresia    = models.TextField(max_length=30)



    def __str__(self):
        return f'Tipo de Membresía: {self.nombre_membresia}, ID: {self.id_tipo_membresia}'


class Membresia(models.Model):
    id_membresia        = models.AutoField(primary_key = True)
    tipo_membresia      = models.ForeignKey(TipoMembresia, on_delete = models.PROTECT)
    usuario_asociado    = models.ForeignKey(Usuario,on_delete=models.PROTECT)
    activa              = models.BooleanField()
    fecha_creacion      = models.DateField(auto_now_add = True)
    fecha_modificacion  = models.DateField(auto_now = True)

    class Meta:
        ordering = ['-id_membresia']
    def __str__(self):
        return (f'Membresía ID: {self.id_membresia}, Usuario: {self.usuario_asociado.username}, '
                f'Tipo: {self.tipo_membresia.nombre_membresia}, Activa: {self.activa}, '
                f'Fecha creación: {self.fecha_creacion}, Última modificación: {self.fecha_modificacion}')


class Asignatura(models.Model):
    id_asignatura       = models.AutoField(primary_key=True)
    nombre_asignatura   = models.TextField(max_length=30)
    desc_asignatura     = QuillField()
    fecha_creacion      = models.DateField(auto_now_add=True)
    profesor            = models.ForeignKey(Usuario,on_delete= models.PROTECT)
    activa              = models.BooleanField()
    duracion            = models.IntegerField(help_text="Duración en semanas", null=True, blank=True)
    cupos_maximos       = models.PositiveIntegerField(default=30)
    horario             = models.TextField(null=True, blank=True)

    def __str__(self):
        return (f'Asignatura: {self.nombre_asignatura}, Profesor: {self.profesor.username}, '
                f'Fecha creación: {self.fecha_creacion}')



class AsignaturaXAlumno(models.Model):
    id_asignaturaxalmnos= models.AutoField(primary_key = True)
    id_asignatura_rel   = models.ForeignKey(Asignatura,on_delete = models.PROTECT)
    id_alumno_usuario   = models.ForeignKey(Usuario,on_delete = models.PROTECT)
    fecha_inscripcion   = models.DateField(auto_now_add=True)
    promedio_notas      = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)

    ESTADOS = [
        ('inscrito', 'Inscrito'),
        ('en curso', 'En curso'),
        ('completado', 'Completado'),
        ('abandonado', 'Abandonado'),
    ]

    estado_inscripcion = models.CharField(max_length=20, choices=ESTADOS, default='inscrito')

    def __str__(self):
        return (f'Asignatura: {self.id_asignatura_rel.nombre_asignatura}, '
                f'Alumno: {self.id_alumno_usuario.username}')


class UnidadClase(models.Model):
    id_unidad_clase     = models.AutoField(primary_key=True)
    nombre_unidad       = models.TextField(max_length=200)
    fecha_creacion      = models.DateField(auto_now_add=True)
    descripcion = models.TextField(null=True, blank=True)
    numero_orden = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'Unidad de Clase: {self.nombre_unidad}, Fecha creación: {self.fecha_creacion}'

class ContenidoClase(models.Model):
    id_contenido        = models.AutoField(primary_key = True)
    fecha_creacion      = models.DateField(auto_now_add=True)
    id_asignatura       = models.ForeignKey(Asignatura,on_delete=models.PROTECT)
    contenido_clases    = QuillField()
    unidad_asociada     = models.ForeignKey(UnidadClase,on_delete=models.PROTECT)
    fecha_creacion      = models.DateField(auto_now_add=True)

    def __str__(self):
        return (f'Contenido de clase ID: {self.id_contenido}, Asignatura: {self.id_asignatura.nombre_asignatura}, '
                f'Unidad: {self.unidad_asociada.nombre_unidad}, Fecha creación: {self.fecha_creacion}')

class Asistencia(models.Model):
    id_asistencia       = models.AutoField(primary_key=True)
    alumno_asociado     = models.ForeignKey(Usuario, on_delete=models.PROTECT)
    confirmacion        = models.BooleanField()
    asignatura_alumno   = models.ForeignKey(AsignaturaXAlumno, on_delete=models.PROTECT)
    fecha_asistencia    = models.DateTimeField(auto_now_add=True)
    motivo_ausencia     = models.TextField(null=True, blank=True)

    def clean(self):
        # Verificar que el alumno en AsignaturaXAlumnos sea el mismo que en alumno_asociado
        if self.alumno_asociado != self.asignatura_alumno.id_alumno_usuario:
            raise ValidationError('El alumno no está inscrito en esta asignatura.')
        

    def __str__(self):
        return (f'Asistencia ID: {self.id_asistencia}, Alumno: {self.alumno_asociado.username}, '
                f'Asignatura: {self.asignatura_alumno.id_asignatura_rel.nombre_asignatura}, '
                f'Confirmación: {self.confirmacion}')

class Evaluacion(models.Model):
    id_evaluacion       = models.AutoField(primary_key=True)
    asignatura_alumno   = models.ForeignKey(AsignaturaXAlumno, on_delete=models.PROTECT)
    nombre_evaluacion   = models.CharField(max_length=100)
    descripcion         = models.TextField(null=True, blank=True)
    fecha_evaluacion    = models.DateField(auto_now_add=True)
    nota                = models.DecimalField(max_digits=1, decimal_places=1)  # Nota sobre 10, por ejemplo
    ponderacion         = models.DecimalField(max_digits=4, decimal_places=2, default=1.0, help_text="Ponderación de la nota")  # Permite dar mayor valor a ciertas evaluaciones
    fecha_creacion      = models.DateField(auto_now_add=True)
    def clean(self):
        # Verificar que el alumno en AsignaturaXAlumnos sea el mismo que en alumno_asociado
        if self.alumno_asociado != self.asignatura_alumno.id_alumno_usuario:
            raise ValidationError('El alumno no está inscrito en esta asignatura.')
        
    def __str__(self):
        return f'Evaluación: {self.nombre_evaluacion} - Alumno: {self.asignatura_alumno.id_alumno_usuario.username} - Nota: {self.nota}'


class GrabacionClase(models.Model):
    id_grabacion = models.AutoField(primary_key=True)
    asignatura = models.ForeignKey(Asignatura, on_delete=models.PROTECT)
    fecha_grabacion = models.DateTimeField(auto_now_add=True)
    video = models.FileField(upload_to='videos_clases/')  # Ruta de almacenamiento del video

    def __str__(self):
        return f'Grabación de clase ID: {self.id_grabacion}, Asignatura: {self.asignatura.nombre_asignatura}, Fecha: {self.fecha_grabacion}'