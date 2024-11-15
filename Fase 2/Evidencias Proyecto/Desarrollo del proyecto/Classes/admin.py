from django.contrib import admin
from .models import (
    TipoMembresia,
    Membresia,
    Asignatura,
    AsignaturaXAlumno,
    UnidadClase,
    ContenidoClase,
    Clase,
    Asistencia,
    Evaluacion
)

# Configuración de los modelos en el panel de administración

@admin.register(TipoMembresia)
class TipoMembresiaAdmin(admin.ModelAdmin):
    list_display = ('id_tipo_membresia', 'nombre_membresia')
    search_fields = ('nombre_membresia',)


@admin.register(Membresia)
class MembresiaAdmin(admin.ModelAdmin):
    list_display = ('id_membresia', 'tipo_membresia', 'usuario_asociado', 'activa', 'fecha_creacion')
    list_filter = ('activa', 'fecha_creacion', 'tipo_membresia')
    search_fields = ('usuario_asociado__username', 'tipo_membresia__nombre_membresia')


@admin.register(Asignatura)
class AsignaturaAdmin(admin.ModelAdmin):
    list_display = ('id_asignatura', 'nombre_asignatura', 'profesor', 'activa', 'fecha_creacion')
    list_filter = ('activa', 'fecha_creacion', 'profesor')
    search_fields = ('nombre_asignatura', 'profesor__username')


@admin.register(AsignaturaXAlumno)
class AsignaturaXAlumnoAdmin(admin.ModelAdmin):
    list_display = ('id_asignaturaxalmnos', 'id_asignatura_rel', 'id_alumno_usuario', 'estado_inscripcion', 'promedio_notas', 'fecha_inscripcion')
    list_filter = ('estado_inscripcion', 'fecha_inscripcion', 'id_asignatura_rel')
    search_fields = ('id_asignatura_rel__nombre_asignatura', 'id_alumno_usuario__username')


@admin.register(UnidadClase)
class UnidadClaseAdmin(admin.ModelAdmin):
    list_display = ('id_unidad_clase', 'nombre_unidad', 'materia_asociada', 'numero_orden', 'fecha_creacion')
    list_filter = ('materia_asociada', 'fecha_creacion')
    search_fields = ('nombre_unidad', 'materia_asociada__nombre_asignatura')


@admin.register(ContenidoClase)
class ContenidoClaseAdmin(admin.ModelAdmin):
    list_display = ('id_contenido', 'titulo_contenido', 'unidad_asociada', 'fecha_creacion')
    list_filter = ('unidad_asociada', 'fecha_creacion')
    search_fields = ('titulo_contenido', 'unidad_asociada__nombre_unidad')


@admin.register(Clase)
class ClaseAdmin(admin.ModelAdmin):
    list_display = ('id_clase', 'nombre_contenido', 'asignatura', 'fecha_clase', 'inicio_clase', 'final_clase')
    list_filter = ('fecha_clase', 'asignatura')
    search_fields = ('nombre_contenido', 'asignatura__nombre_asignatura')


@admin.register(Asistencia)
class AsistenciaAdmin(admin.ModelAdmin):
    list_display = ('id_asistencia', 'clase_asistencia', 'asignatura_alumno', 'confirmacion', 'fecha_asistencia')
    list_filter = ('confirmacion', 'fecha_asistencia', 'clase_asistencia')
    search_fields = ('clase_asistencia__nombre_contenido', 'asignatura_alumno__id_asignatura_rel__nombre_asignatura')


@admin.register(Evaluacion)
class EvaluacionAdmin(admin.ModelAdmin):
    list_display = ('id_evaluacion', 'asignatura_alumno', 'nombre_evaluacion', 'nota', 'ponderacion', 'fecha_evaluacion')
    list_filter = ('fecha_evaluacion', 'ponderacion')
    search_fields = ('nombre_evaluacion', 'asignatura_alumno__id_alumno_usuario__username')
