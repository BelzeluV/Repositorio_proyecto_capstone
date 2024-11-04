
# Register your models here.
from django.contrib import admin
from Library.models import Instrumento, MaterialBiblioteca, mensajebiblioteca

# Configuración de Instrumento
@admin.register(Instrumento)
class InstrumentoAdmin(admin.ModelAdmin):
    list_display = ('id_instrumento', 'nombre_instrumento', 'fecha_creacion', 'imagen_referencial')
    search_fields = ('nombre_instrumento',)
    list_filter = ('fecha_creacion',)

# Configuración de MaterialBiblioteca
@admin.register(MaterialBiblioteca)
class MaterialBibliotecaAdmin(admin.ModelAdmin):
    list_display = (
        'titulo_material','id_material', 'contenidomaterial', 'fecha_creacion', 
        'imagen_referencia', 'instrumento', 'usuario_creador'
    )
    search_fields = ('contenidomaterial', 'instrumento__nombre_instrumento')
    list_filter = ('fecha_creacion', 'instrumento')

# Configuración de mensajebiblioteca
@admin.register(mensajebiblioteca)
class MensajeBibliotecaAdmin(admin.ModelAdmin):
    list_display = ('id_mensaje', 'mensaje', 'creado_por_usuario')
    search_fields = ('mensaje', 'creado_por_usuario__username')
    list_filter = ('creado_por_usuario',)
