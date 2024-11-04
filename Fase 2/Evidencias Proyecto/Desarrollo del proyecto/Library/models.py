from django.db import models
from django_quill.fields import QuillField
from Store.models import Usuario

# Create your models here.
class Instrumento(models.Model):
    id_instrumento      = models.AutoField(primary_key=True)
    nombre_instrumento  = models.TextField(max_length=30)
    fecha_creacion      = models.DateField(auto_now_add=True)
    imagen_referencial  = models.ImageField(models.ImageField(upload_to = "instrumentobiblioteca",null = True, default= 0))

class MaterialBiblioteca(models.Model):
    id_material         = models.AutoField(primary_key=True)
    titulo_material     = models.TextField(max_length=100)
    nivel_aprendizaje   = models.IntegerField()
    subtitulo_material  = models.TextField(max_length=300)
    contenidomaterial   = QuillField()
    fecha_creacion      = models.DateField(auto_now_add=True)
    imagen_referencia   = models.ImageField(models.ImageField(upload_to = "MaterialBiblioteca",null = True))
    instrumento         = models.ForeignKey(Instrumento, on_delete = models.PROTECT)
    usuario_creador     = models.ForeignKey(Usuario, on_delete= models.PROTECT)

class mensajebiblioteca(models.Model):
    id_mensaje          = models.AutoField(primary_key=True)
    mensaje             = QuillField()
    creado_por_usuario  = models.ForeignKey(Usuario, on_delete=models.CASCADE)
