# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser

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
        return self.username
    


class Proveedor(models.Model):
    id_proveedor        = models.AutoField(primary_key = True)
    nombreproveedor     = models.CharField(max_length = 50)
    direccion           = models.CharField(max_length = 100)
    telefono            = models.CharField(default = '', max_length = 15)
    email               = models.EmailField()
    fecha_registro      = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return  self.nombreproveedor

class TipoProducto(models.Model):
    id_tipo             = models.AutoField(primary_key = True)
    nombretipo          = models.CharField(max_length = 30, unique = True, error_messages = {"unique" : "Esta tipo de producto ya está registrado"})

    def __str__(self):
        return self.nombretipo

class Categoria(models.Model):
    id_categoria        = models.AutoField(primary_key = True)
    nombrecategoria     = models.CharField(max_length = 30, unique = True, error_messages = {"unique" : "Esta categoria ya está registrada"})
    tipo_producto       = models.ForeignKey(TipoProducto,on_delete = models.PROTECT)
    def __str__(self):
        return self.nombrecategoria
    
class Subcategoria(models.Model):
    id_subcategoria     = models.AutoField(primary_key = True)
    nombre_subcategoria = models.CharField(max_length = 30, unique = True, error_messages = {"unique" : "Esta subcategoria ya está registrada"})
    categoria           = models.ForeignKey(Categoria, on_delete = models.PROTECT)
    def __str__(self):
        return self.nombre_subcategoria

class Marca(models.Model):
    id_marca            = models.AutoField(primary_key = True)
    nombre_marca        = models.CharField(max_length = 40)
    def __str__(self):
        return self.nombre_marca

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

    def __str__(self): 
        return self.nombre_producto

##modelos de las ordenes de servicio
class Orden(models.Model):
    id_orden            = models.AutoField(primary_key = True)
    descripcion         = models.CharField(max_length = 500)
    nombre_dueño        = models.CharField(max_length = 50, null=True)
    estado              = models.IntegerField(default = 0, choices = opcionEstado)
    fecha_creacion      = models.DateField(null = True)
    usuario_rel         = models.ForeignKey(Usuario, on_delete= models.PROTECT)
    def __str__(self):
        return f'{self.id_orden}'

class Ordenxproducto(models.Model):
    id_ordenxproducto   = models.AutoField(primary_key=True)
    id_orden_relacion   = models.ForeignKey(Orden, on_delete = models.CASCADE)
    id_producto         = models.ForeignKey(Producto, on_delete = models.CASCADE)
    cantidad            = models.IntegerField()

    class Meta:
        ordering = ['-id_ordenxproducto']

    def __str__(self):
        return (f'Orden: {self.id_orden_relacion}, Producto relacionado: {self.id_producto}').format(**self.__dict__)