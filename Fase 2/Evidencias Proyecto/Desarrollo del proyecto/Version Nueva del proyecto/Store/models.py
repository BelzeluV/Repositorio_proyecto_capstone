# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser
from django_quill.fields import QuillField
from django.core.validators import MinValueValidator, MaxValueValidator


opcionEstado = [
    [0,"empacando"],
    [1,"esperando viaje"],
    [2,"enviado"],
    [3,"entregado"],
    [4,"cancelado"],

]
opcionesSexo = [
    [0,"hombre"],
    [1,"Mujer"],
    [2,"sin especificar"]
]
regiones = [
    [0, "seleccione..."],
    [1, "Arica y Parinacota"],
    [2, "Tarapacá"],
    [3, "Antofagasta"],
    [4, "Atacama"],
    [5, "Coquimbo"],
    [6, "Valparaíso"],
    [7, "Región Metropolitana de Santiago"],
    [8, "Región del Libertador General Bernardo O'Higgins"],
    [9, "Región del Maule"],
    [10, "Región de Ñuble"],
    [11, "Región del Biobío"],
    [12, "Región de La Araucanía"],
    [13, "Región de Los Ríos"],
    [14, "Región de Los Lagos"],
    [15, "Región de Aysén del General Carlos Ibáñez del Campo"],
    [16, "Región de Magallanes y de la Antártica Chilena"]
]
comunas = [
    [1, "Cerrillos"],
    [2, "Cerro Navia"],
    [3, "Conchalí"],
    [4, "El Bosque"],
    [5, "Estación Central"],
    [6, "Huechuraba"],
    [7, "Independencia"],
    [8, "La Cisterna"],
    [9, "La Florida"],
    [10, "La Granja"],
    [11, "La Pintana"],
    [12, "La Reina"],
    [13, "Las Condes"],
    [14, "Lo Barnechea"],
    [15, "Lo Espejo"],
    [16, "Lo Prado"],
    [17, "Macul"],
    [18, "Maipú"],
    [19, "Ñuñoa"],
    [20, "Pedro Aguirre Cerda"],
    [21, "Peñalolén"],
    [22, "Providencia"],
    [23, "Pudahuel"],
    [24, "Quilicura"],
    [25, "Quinta Normal"],
    [26, "Recoleta"],
    [27, "Renca"],
    [28, "San Joaquín"],
    [29, "San Miguel"],
    [30, "San Ramón"],
    [31, "Santiago Centro"],
    [32, "Vitacura"],
    [33, "Puente Alto"],
    [34, "San Bernardo"],
    [35, "Pirque"],
    [36, "San José de Maipo"],
    [37, "Colina"],
    [38, "Lampa"],
    [39, "Tiltil"],
    [40, "Buin"],
    [41, "Calera de Tango"],
    [42, "Paine"],
    [43, "Melipilla"],
    [44, "Curacaví"],
    [45, "María Pinto"],
    [46, "San Pedro"],
    [47, "Talagante"],
    [48, "El Monte"],
    [49, "Isla de Maipo"],
    [50, "Padre Hurtado"],
    [51, "Peñaflor"]
]

class Usuario(AbstractUser):
    RUT                 = models.CharField(default = '', max_length = 13,  unique = True, error_messages = {"unique": "El rut ya está registrado."}, blank=True)
    nacimiento          = models.DateField(null = True)
    genero              = models.IntegerField(default = 2, choices = opcionesSexo)
    telefono            = models.CharField(default = '', max_length = 15)
    direccion           = models.CharField(default = '', max_length = 300)
    region              = models.IntegerField(null = True, blank = True, choices = regiones)  
    comuna              = models.IntegerField(null = True, blank = True, choices = comunas)  
    foto_de_Usuario     = models.ImageField(upload_to = "usuarios",null = True)

    class Meta:
        ordering = ['username']

    def __str__(self):
        return f'Usuario: {self.username}, RUT: {self.RUT}, Genero: {self.genero}, Teléfono: {self.telefono}, Dirección: {self.direccion}, Región: {self.region}, Comuna: {self.comuna}'


    


class Proveedor(models.Model):
    id_proveedor        = models.AutoField(primary_key = True)
    nombreproveedor     = models.CharField(max_length = 50)
    direccion           = models.CharField(max_length = 100)
    telefono            = models.CharField(default = '', max_length = 15)
    email               = models.EmailField()
    fecha_registro      = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Proveedor: {self.nombreproveedor}, Dirección: {self.direccion}, Teléfono: {self.telefono}, Email: {self.email}, Fecha de registro: {self.fecha_registro}'



class TipoProducto(models.Model):
    id_tipo             = models.AutoField(primary_key = True)
    nombretipo          = models.CharField(max_length = 30, unique = True, error_messages = {"unique" : "Esta tipo de producto ya está registrado"})

    def __str__(self):
        return f'TipoProducto: {self.nombretipo}, ID: {self.id_tipo}'



class Categoria(models.Model):
    id_categoria        = models.AutoField(primary_key = True)
    nombrecategoria     = models.CharField(max_length = 30, unique = True, error_messages = {"unique" : "Esta categoria ya está registrada"})
    tipo_producto       = models.ForeignKey(TipoProducto,on_delete = models.PROTECT)

    def __str__(self):
        return f'Categoría: {self.nombrecategoria}, Tipo de producto: {self.tipo_producto.nombretipo}, ID: {self.id_categoria}'


    
class Subcategoria(models.Model):
    id_subcategoria     = models.AutoField(primary_key = True)
    nombre_subcategoria = models.CharField(max_length = 30, unique = True, error_messages = {"unique" : "Esta subcategoria ya está registrada"})
    categoria           = models.ForeignKey(Categoria, on_delete = models.PROTECT)
    def __str__(self):
        return f'Subcategoría: {self.nombre_subcategoria}, Categoría: {self.categoria.nombrecategoria}, ID: {self.id_subcategoria}'




class Marca(models.Model):
    id_marca            = models.AutoField(primary_key = True)
    nombre_marca        = models.CharField(max_length = 40)
    def __str__(self):
        return f'Marca: {self.nombre_marca}, ID: {self.id_marca}'


class Producto(models.Model):
    id_producto         = models.AutoField(primary_key = True)
    SKU                 = models.CharField(max_length = 10, unique = True, error_messages = {"unique" : "Este SKU ya está registrado"})
    nombre_producto     = models.CharField(max_length = 60)
    descripcion         = models.TextField(max_length = 1000,null=True)
    Precio_compra       = models.IntegerField()
    precio_venta        = models.IntegerField()
    precio_oferta       = models.IntegerField(blank = True)
    stock               = models.IntegerField()
    marca               = models.ForeignKey(Marca, on_delete = models.PROTECT, null = True)
    tipo_producto       = models.ForeignKey(TipoProducto, on_delete = models.PROTECT, null = True)
    categoria_producto  = models.ForeignKey(Categoria, on_delete = models.PROTECT, null = True)
    subcat_producto     = models.ForeignKey(Subcategoria, on_delete = models.PROTECT, null = True)
    proveedor           = models.ForeignKey(Proveedor, on_delete = models.PROTECT, null = True)
    imagen_producto     = models.ImageField(upload_to = "productos", blank = True, null=True)
    activo              = models.BooleanField(default = True)

    class Meta:
        ordering = ['id_producto']

    def __str__(self):
        return (f'Producto: {self.nombre_producto}, SKU: {self.SKU}, '
                f'Precio compra: {self.Precio_compra}, Precio venta: {self.precio_venta}, '
                f'Stock: {self.stock}, Marca: {self.marca.nombre_marca}, '
                f'Proveedor: {self.proveedor.nombreproveedor}')

class Valoracion(models.Model):
    id_valoracion       = models.AutoField(primary_key=True)
    cantidad_estrellas  = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    desc_valoracion     = QuillField()
    usuario_validacion  = models.ForeignKey(Usuario, on_delete=models.PROTECT)
    producto_valorado   = models.ForeignKey(Producto,on_delete=models.PROTECT)

    class Meta:
        ordering = ['-id_valoracion']

    def __str__(self):
        return (f'Valoración de {self.usuario_validacion.username} para el producto '
                f'{self.producto_valorado.nombre_producto}, Estrellas: {self.cantidad_estrellas}, '
                f'Descripción: {self.desc_valoracion}')


##modelos de las ordenes de servicio
class Orden(models.Model):
    id_orden            = models.AutoField(primary_key = True)
    descripcion         = models.CharField(max_length = 500)
    nombre_comprador    = models.CharField(max_length = 50, null=True)
    direccion_entrega   = models.TextField(max_length=300)
    estado              = models.IntegerField(default = 0, choices = opcionEstado)
    fecha_creacion      = models.DateField(null = True)
    usuario_rel         = models.ForeignKey(Usuario, on_delete= models.PROTECT)
    
    class Meta:
        ordering = ['-id_orden']

    def __str__(self):
        return (f'Orden ID: {self.id_orden}, Usuario: {self.usuario_rel.username}, '
                f'Dirección de entrega: {self.direccion_entrega}, Estado: {self.estado}, '
                f'Fecha creación: {self.fecha_creacion}')


class Ordenxproducto(models.Model):
    id_ordenxproducto   = models.AutoField(primary_key = True)
    id_orden_relacion   = models.ForeignKey(Orden, on_delete = models.PROTECT)
    id_producto         = models.ForeignKey(Producto, on_delete = models.PROTECT)
    valorado            = models.BooleanField()
    cantidad            = models.IntegerField()

    class Meta:
        ordering = ['-id_ordenxproducto']

    def __str__(self):
        return (f'Orden: {self.id_orden_relacion.id_orden}, Producto: {self.id_producto.nombre_producto}, '
                f'Cantidad: {self.cantidad}, Valoración: {self.valorado}')


class MensajeOrden(models.Model):
    id_mensaje          = models.AutoField(primary_key = True)
    titulo_mensaje      = models.TextField(max_length=40)
    contenido_mensaje   = QuillField()
    fecha_creacion      = models.DateField(auto_now_add = True)
    id_orden_asociada   = models.ForeignKey(Orden,on_delete= models.PROTECT)
    id_usuario_creador  = models.ForeignKey(Usuario,on_delete=models.PROTECT)

    class Meta: 
        ordering = ['-id_mensaje']
    def __str__(self):
        return (f'Mensaje ID: {self.id_mensaje}, Título: {self.titulo_mensaje}, '
                f'Fecha creación: {self.fecha_creacion}, '
                f'Orden ID: {self.id_orden_asociada.id_orden}, Usuario: {self.id_usuario_creador.username}')



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

    def __str__(self):
        return (f'Asignatura: {self.nombre_asignatura}, Profesor: {self.profesor.username}, '
                f'Fecha creación: {self.fecha_creacion}')



class AsignaturaXAlumnos(models.Model):
    id_asignaturaxalmnos= models.AutoField(primary_key = True)
    id_asignatura_rel   = models.ForeignKey(Asignatura,on_delete = models.PROTECT)
    id_alumno_usuario   = models.ForeignKey(Usuario,on_delete = models.PROTECT)

    def __str__(self):
        return (f'Asignatura: {self.id_asignatura_rel.nombre_asignatura}, '
                f'Alumno: {self.id_alumno_usuario.username}')


class UnidadClases(models.Model):
    id_unidad_clase     = models.AutoField(primary_key=True)
    nombre_unidad       = models.TextField(max_length=200)
    fecha_creacion      = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'Unidad de Clase: {self.nombre_unidad}, Fecha creación: {self.fecha_creacion}'

class ContenidoClases(models.Model):
    id_contenido        = models.AutoField(primary_key = True)
    fecha_creacion      = models.DateField(auto_now_add=True)
    id_asignatura       = models.ForeignKey(Asignatura,on_delete=models.PROTECT)
    contenido_clases    = QuillField()
    unidad_asociada     = models.ForeignKey(UnidadClases,on_delete=models.PROTECT)
    fecha_creacion      = models.DateField(auto_now_add=True)

    def __str__(self):
        return (f'Contenido de clase ID: {self.id_contenido}, Asignatura: {self.id_asignatura.nombre_asignatura}, '
                f'Unidad: {self.unidad_asociada.nombre_unidad}, Fecha creación: {self.fecha_creacion}')
class Asistencia(models.Model):
    id_asistencia       = models.AutoField(primary_key=True)
    
