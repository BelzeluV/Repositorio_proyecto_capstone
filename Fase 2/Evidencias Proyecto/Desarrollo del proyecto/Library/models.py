from django.db import models
from django_quill.fields import QuillField
from Store.models import Usuario

# Create your models here.from django.db import models # Asegúrate de importar QuillField si es necesario en tu proyecto.segúrate de importar QuillField si es necesario en tu proyecto.

class Instrumento(models.Model):
    id_instrumento      = models.AutoField(primary_key=True)
    nombre_instrumento  = models.TextField(max_length=30, default="Instrumento desconocido")
    fecha_creacion      = models.DateField(auto_now_add=True)
    imagen_referencial  = models.ImageField(upload_to="instrumentobiblioteca", null=True, default="default.jpg")
    
    def __str__(self):
        return f"{self.nombre_instrumento}"


class MaterialBiblioteca(models.Model):
    id_material         = models.AutoField(primary_key=True)
    titulo_material     = models.TextField(max_length=100, default="Título desconocido")
    nivel_aprendizaje   = models.IntegerField(default=1)
    subtitulo_material  = models.TextField(max_length=300, default="Subtítulo no disponible")
    contenidomaterial   = QuillField(default="Contenido en construcción")
    fecha_creacion      = models.DateField(auto_now_add=True)
    imagen_referencia   = models.ImageField(upload_to="MaterialBiblioteca", null=True, default="default.jpg")
    instrumento         = models.ForeignKey(Instrumento, on_delete=models.PROTECT)
    usuario_creador     = models.ForeignKey(Usuario, on_delete=models.PROTECT)  # Asegúrate de que "Usuario" esté bien definido
    cantidad_likes      = models.IntegerField(default=0)
    cantidad_dislikes   = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.titulo_material}"


class MensajeBiblioteca(models.Model):
    id_mensaje          = models.AutoField(primary_key=True)
    mensaje             = QuillField()
    creado_por_usuario  = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    material_asociado   = models.ForeignKey(MaterialBiblioteca, on_delete=models.PROTECT)
    fecha_creacion      = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.mensaje}"  # Limitar el texto de vista previa para mayor claridad

