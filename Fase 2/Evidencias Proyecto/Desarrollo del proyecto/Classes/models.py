from django.db import models
from Store.models import Usuario
from django_quill.fields import QuillField
from django.core.exceptions import ValidationError

'''
class Usuario(AbstractUser):
    RUT                 = models.CharField(default = '', max_length = 13,  unique = True, error_messages = {"unique": "El rut ya está registrado."}, blank=True)
    nacimiento          = models.DateField(null = True)
    genero              = models.IntegerField(default = 2, choices = opcionesSexo)
    telefono            = models.CharField(default = '', max_length = 15)
    direccion           = models.CharField(default = '', max_length = 300)
    region              = models.IntegerField(null = True, blank = True, choices = regiones)  
    comuna              = models.IntegerField(null = True, blank = True, choices = comunas)  
    foto_de_Usuario     = models.ImageField(upload_to = "usuarios",null = True)
    es_profesor         = models.BooleanField(default=False)
    es_admin_biblioteca = models.BooleanField(default=False)

    class Meta:
        ordering = ['username']

    def __str__(self):
        return f'{self.username}'

'''
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
    imagen_asignatura   = models.ImageField(upload_to='asignaturas')
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

    estado_inscripcion  = models.CharField(max_length=20, choices=ESTADOS, default='inscrito')

    def __str__(self):
        return (f'Asignatura: {self.id_asignatura_rel.nombre_asignatura}, '
                f'Alumno: {self.id_alumno_usuario.username}')


class UnidadClase(models.Model):
    id_unidad_clase     = models.AutoField(primary_key=True)
    nombre_unidad       = models.TextField(max_length=200)
    fecha_creacion      = models.DateField(auto_now_add=True)
    descripcion         = models.TextField(null=True, blank=True)
    numero_orden        = models.PositiveIntegerField(default=1)
    materia_asociada    = models.ForeignKey(Asignatura,on_delete=models.PROTECT)
    imagenclase         = models.ImageField(upload_to='unidades')
    def __str__(self):
        return f'Unidad de Clase: {self.nombre_unidad}, Fecha creación: {self.fecha_creacion}'

class ContenidoClase(models.Model):
    id_contenido        = models.AutoField(primary_key = True)
    fecha_creacion      = models.DateField(auto_now_add=True)
    titulo_contenido    = models.TextField(max_length=60)
    subtitulo_contenido = models.TextField(max_length=150)
    contenido_clases    = QuillField()
    unidad_asociada     = models.ForeignKey(UnidadClase,on_delete=models.PROTECT)
    fecha_creacion      = models.DateField(auto_now_add=True)

    def __str__(self):
        return (f'Contenido de clase ID: {self.id_contenido}'
                f'Unidad: {self.unidad_asociada.nombre_unidad}, Fecha creación: {self.fecha_creacion}')



class Clase(models.Model):
    id_clase            = models.AutoField(primary_key=True)
    nombre_contenido    = models.TextField(max_length = 30)
    activa              = models.BooleanField(default=True)
    fecha_clase         = models.DateField()
    inicio_clase        = models.TimeField()
    final_clase         = models.TimeField()
    asignatura          = models.ForeignKey(Asignatura, on_delete=models.PROTECT)
    video               = models.FileField(upload_to='videos_clases/')  # Ruta de almacenamiento del video
    invitacion_zoom_link= models.TextField(max_length=500)
    def __str__(self):
        return f'Clase: {self.nombre_contenido} - Fecha: {self.fecha_clase} - Asignatura: {self.asignatura.nombre_asignatura}'


class Asistencia(models.Model):
    id_asistencia       = models.AutoField(primary_key=True)
    clase_asistencia    = models.ForeignKey(Clase, on_delete=models.PROTECT)
    asignatura_alumno   = models.ForeignKey(AsignaturaXAlumno, on_delete=models.PROTECT)
    confirmacion        = models.BooleanField()
    motivo_ausencia     = models.TextField(null=True, blank=True)
    fecha_asistencia    = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('clase_asistencia', 'asignatura_alumno')

    def clean(self):
        # Verificar que la clase y la asignatura del alumno coincidan
        if self.clase_asistencia.asignatura != self.asignatura_alumno.id_asignatura_rel:
            raise ValidationError('La asistencia no corresponde a la asignatura de este alumno.')

    def __str__(self):
        return (f'Asistencia ID: {self.id_asistencia}, Alumno: {self.asignatura_alumno.id_alumno_usuario.username}, '
                f'Clase: {self.clase_asistencia.nombre_contenido}, Confirmación: {self.confirmacion}')

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
