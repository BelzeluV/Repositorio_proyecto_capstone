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
    [0,"Hombre"],
    [1,"Mujer"],
    [2,"sin especificar"]
]


regiones = [
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
    [1, "Cerrillos", "Metropolitana"],
    [2, "Cerro Navia", "Metropolitana"],
    [3, "Conchalí", "Metropolitana"],
    [4, "El Bosque", "Metropolitana"],
    [5, "Estación Central", "Metropolitana"],
    [6, "Huechuraba", "Metropolitana"],
    [7, "Independencia", "Metropolitana"],
    [8, "La Cisterna", "Metropolitana"],
    [9, "La Florida", "Metropolitana"],
    [10, "La Granja", "Metropolitana"],
    [11, "La Pintana", "Metropolitana"],
    [12, "La Reina", "Metropolitana"],
    [13, "Las Condes", "Metropolitana"],
    [14, "Lo Barnechea", "Metropolitana"],
    [15, "Lo Espejo", "Metropolitana"],
    [16, "Lo Prado", "Metropolitana"],
    [17, "Macul", "Metropolitana"],
    [18, "Maipú", "Metropolitana"],
    [19, "Ñuñoa", "Metropolitana"],
    [20, "Pedro Aguirre Cerda", "Metropolitana"],
    [21, "Peñalolén", "Metropolitana"],
    [22, "Providencia", "Metropolitana"],
    [23, "Pudahuel", "Metropolitana"],
    [24, "Quilicura", "Metropolitana"],
    [25, "Quinta Normal", "Metropolitana"],
    [26, "Recoleta", "Metropolitana"],
    [27, "Renca", "Metropolitana"],
    [28, "San Joaquín", "Metropolitana"],
    [29, "San Miguel", "Metropolitana"],
    [30, "San Ramón", "Metropolitana"],
    [31, "Santiago Centro", "Metropolitana"],
    [32, "Vitacura", "Metropolitana"],
    [33, "Puente Alto", "Metropolitana"],
    [34, "San Bernardo", "Metropolitana"],
    [35, "Pirque", "Metropolitana"],
    [36, "San José de Maipo", "Metropolitana"],
    [37, "Colina", "Metropolitana"],
    [38, "Lampa", "Metropolitana"],
    [39, "Tiltil", "Metropolitana"],
    [40, "Buin", "Metropolitana"],
    [41, "Calera de Tango", "Metropolitana"],
    [42, "Paine", "Metropolitana"],
    [43, "Melipilla", "Metropolitana"],
    [44, "Curacaví", "Metropolitana"],
    [45, "María Pinto", "Metropolitana"],
    [46, "San Pedro", "Metropolitana"],
    [47, "Talagante", "Metropolitana"],
    [48, "El Monte", "Metropolitana"],
    [49, "Isla de Maipo", "Metropolitana"],
    [50, "Padre Hurtado", "Metropolitana"],
    [51, "Peñaflor", "Metropolitana"]
]

'''

comunas = [
    # Región de Arica y Parinacota (1)
    [1, "Arica", 1],
    [2, "Camarones", 1],
    [3, "Putre", 1],
    [4, "General Lagos", 1],

    # Región de Tarapacá (2)
    [5, "Iquique", 2],
    [6, "Alto Hospicio", 2],
    [7, "Pozo Almonte", 2],
    [8, "Huara", 2],
    [9, "Camiña", 2],
    [10, "Colchane", 2],
    [11, "Pica", 2],

    # Región de Antofagasta (3)
    [12, "Antofagasta", 3],
    [13, "Mejillones", 3],
    [14, "Sierra Gorda", 3],
    [15, "Taltal", 3],
    [16, "Calama", 3],
    [17, "Ollagüe", 3],
    [18, "San Pedro de Atacama", 3],

    # Región de Atacama (4)
    [19, "Copiapó", 4],
    [20, "Caldera", 4],
    [21, "Tierra Amarilla", 4],
    [22, "Chañaral", 4],
    [23, "Diego de Almagro", 4],
    [24, "Vallenar", 4],
    [25, "Freirina", 4],
    [26, "Huasco", 4],

    # Región de Coquimbo (5)
    [27, "La Serena", 5],
    [28, "Coquimbo", 5],
    [29, "Andacollo", 5],
    [30, "La Higuera", 5],
    [31, "Paiguano", 5],
    [32, "Vicuña", 5],
    [33, "Illapel", 5],
    [34, "Canela", 5],
    [35, "Los Vilos", 5],
    [36, "Salamanca", 5],
    [37, "Ovalle", 5],
    [38, "Combarbalá", 5],
    [39, "Monte Patria", 5],
    [40, "Punitaqui", 5],
    [41, "Río Hurtado", 5],

    # Región de Valparaíso (6)
    [42, "Valparaíso", 6],
    [43, "Casablanca", 6],
    [44, "Concón", 6],
    [45, "Juan Fernández", 6],
    [46, "Puchuncaví", 6],
    [47, "Quintero", 6],
    [48, "Viña del Mar", 6],
    [49, "Isla de Pascua", 6],
    [50, "Los Andes", 6],
    [51, "Calle Larga", 6],
    [52, "Rinconada", 6],
    [53, "San Esteban", 6],
    [54, "La Ligua", 6],
    [55, "Cabildo", 6],
    [56, "Papudo", 6],
    [57, "Petorca", 6],
    [58, "Zapallar", 6],
    [59, "Quillota", 6],
    [60, "Calera", 6],
    [61, "Hijuelas", 6],
    [62, "La Cruz", 6],
    [63, "Nogales", 6],
    [64, "San Antonio", 6],
    [65, "Algarrobo", 6],
    [66, "Cartagena", 6],
    [67, "El Quisco", 6],
    [68, "El Tabo", 6],
    [69, "Santo Domingo", 6],
    [70, "San Felipe", 6],
    [71, "Catemu", 6],
    [72, "Llaillay", 6],
    [73, "Panquehue", 6],
    [74, "Putaendo", 6],
    [75, "Santa María", 6],

    # Región Metropolitana de Santiago (7)
    [76, "Cerrillos", 7],
    [77, "Cerro Navia", 7],
    [78, "Conchalí", 7],
    [79, "El Bosque", 7],
    [80, "Estación Central", 7],
    [81, "Huechuraba", 7],
    [82, "Independencia", 7],
    [83, "La Cisterna", 7],
    [84, "La Florida", 7],
    [85, "La Granja", 7],
    [86, "La Pintana", 7],
    [87, "La Reina", 7],
    [88, "Las Condes", 7],
    [89, "Lo Barnechea", 7],
    [90, "Lo Espejo", 7],
    [91, "Lo Prado", 7],
    [92, "Macul", 7],
    [93, "Maipú", 7],
    [94, "Ñuñoa", 7],
    [95, "Pedro Aguirre Cerda", 7],
    [96, "Peñalolén", 7],
    [97, "Providencia", 7],
    [98, "Pudahuel", 7],
    [99, "Quilicura", 7],
    [100, "Quinta Normal", 7],
    [101, "Recoleta", 7],
    [102, "Renca", 7],
    [103, "San Joaquín", 7],
    [104, "San Miguel", 7],
    [105, "San Ramón", 7],
    [106, "Santiago", 7],
    [107, "Vitacura", 7],
    [108, "Puente Alto", 7],
    [109, "San Bernardo", 7],
    [110, "Pirque", 7],
    [111, "San José de Maipo", 7],
    [112, "Colina", 7],
    [113, "Lampa", 7],
    [114, "Tiltil", 7],
    [115, "Buin", 7],
    [116, "Calera de Tango", 7],
    [117, "Paine", 7],
    [118, "Melipilla", 7],
    [119, "Curacaví", 7],
    [120, "María Pinto", 7],
    [121, "San Pedro", 7],
    [122, "Talagante", 7],
    [123, "El Monte", 7],
    [124, "Isla de Maipo", 7],
    [125, "Padre Hurtado", 7],
    [126, "Peñaflor", 7],

    # Región del Libertador General Bernardo O'Higgins (8)
    [127, "Rancagua", 8],
    [128, "Codegua", 8],
    [129, "Coinco", 8],
    [130, "Coltauco", 8],
    [131, "Doñihue", 8],
    [132, "Graneros", 8],
    [133, "Las Cabras", 8],
    [134, "Machalí", 8],
    [135, "Malloa", 8],
    [136, "Mostazal", 8],
    [137, "Olivar", 8],
    [138, "Peumo", 8],
    [139, "Pichidegua", 8],
    [140, "Quinta de Tilcoco", 8],
    [141, "Rengo", 8],
    [142, "Requínoa", 8],
    [143, "San Vicente", 8],
    [144, "Pichilemu", 8],
    [145, "La Estrella", 8],
    [146, "Litueche", 8],
    [147, "Marchihue", 8],
    [148, "Navidad", 8],
    [149, "Paredones", 8],
    [150, "San Fernando", 8],
    [151, "Chépica", 8],
    [152, "Chimbarongo", 8],
    [153, "Lolol", 8],
    [154, "Nancagua", 8],
    [155, "Palmilla", 8],
    [156, "Peralillo", 8],
    [157, "Placilla", 8],
    [158, "Pumanque", 8],
    [159, "Santa Cruz", 8],

    # Región del Maule (9)
    [160, "Talca", 9],
    [161, "Constitución", 9],
    [162, "Curepto", 9],
    [163, "Empedrado", 9],
    [164, "Maule", 9],
    [165, "Pelarco", 9],
    [166, "Pencahue", 9],
    [167, "Río Claro", 9],
    [168, "San Clemente", 9],
    [169, "San Rafael", 9],
    [170, "Cauquenes", 9],
    [171, "Chanco", 9],
    [172, "Pelluhue", 9],
    [173, "Curicó", 9],
    [174, "Hualañé", 9],
    [175, "Licantén", 9],
    [176, "Molina", 9],
    [177, "Rauco", 9],
    [178, "Romeral", 9],
    [179, "Sagrada Familia", 9],
    [180, "Teno", 9],
    [181, "Vichuquén", 9],
    [182, "Linares", 9],
    [183, "Colbún", 9],
    [184, "Longaví", 9],
    [185, "Parral", 9],
    [186, "Retiro", 9],
    [187, "San Javier", 9],
    [188, "Villa Alegre", 9],
    [189, "Yerbas Buenas", 9],

    # Región de Ñuble (10)
    [190, "Chillán", 10],
    [191, "Bulnes", 10],
    [192, "Cobquecura", 10],
    [193, "Coelemu", 10],
    [194, "Coihueco", 10],
    [195, "El Carmen", 10],
    [196, "Ninhue", 10],
    [197, "Ñiquén", 10],
    [198, "Pemuco", 10],
    [199, "Pinto", 10],
    [200, "Portezuelo", 10],
    [201, "Quillón", 10],
    [202, "Quirihue", 10],
    [203, "Ránquil", 10],
    [204, "San Carlos", 10],
    [205, "San Fabián", 10],
    [206, "San Ignacio", 10],
    [207, "San Nicolás", 10],
    [208, "Treguaco", 10],
    [209, "Yungay", 10],

    # Región del Biobío (11)
    [210, "Concepción", 11],
    [211, "Coronel", 11],
    [212, "Chiguayante", 11],
    [213, "Florida", 11],
    [214, "Hualqui", 11],
    [215, "Lota", 11],
    [216, "Penco", 11],
    [217, "San Pedro de la Paz", 11],
    [218, "Santa Juana", 11],
    [219, "Talcahuano", 11],
    [220, "Tomé", 11],
    [221, "Hualpén", 11],
    [222, "Lebu", 11],
    [223, "Arauco", 11],
    [224, "Cañete", 11],
    [225, "Contulmo", 11],
    [226, "Curanilahue", 11],
    [227, "Los Álamos", 11],
    [228, "Tirúa", 11],
    [229, "Los Ángeles", 11],
    [230, "Antuco", 11],
    [231, "Cabrero", 11],
    [232, "Laja", 11],
    [233, "Mulchén", 11],
    [234, "Nacimiento", 11],
    [235, "Negrete", 11],
    [236, "Quilaco", 11],
    [237, "Quilleco", 11],
    [238, "San Rosendo", 11],
    [239, "Santa Bárbara", 11],
    [240, "Tucapel", 11],
    [241, "Yumbel", 11],

    # Región de La Araucanía (12)
    [242, "Temuco", 12],
    [243, "Carahue", 12],
    [244, "Cunco", 12],
    [245, "Curarrehue", 12],
    [246, "Freire", 12],
    [247, "Galvarino", 12],
    [248, "Gorbea", 12],
    [249, "Lautaro", 12],
    [250, "Loncoche", 12],
    [251, "Melipeuco", 12],
    [252, "Nueva Imperial", 12],
    [253, "Padre Las Casas", 12],
    [254, "Perquenco", 12],
    [255, "Pitrufquén", 12],
    [256, "Pucón", 12],
    [257, "Saavedra", 12],
    [258, "Teodoro Schmidt", 12],
    [259, "Toltén", 12],
    [260, "Vilcún", 12],
    [261, "Villarrica", 12],
    [262, "Cholchol", 12],
    [263, "Angol", 12],
    [264, "Collipulli", 12],
    [265, "Curacautín", 12],
    [266, "Ercilla", 12],
    [267, "Lonquimay", 12],
    [268, "Los Sauces", 12],
    [269, "Lumaco", 12],
    [270, "Purén", 12],
    [271, "Renaico", 12],
    [272, "Traiguén", 12],
    [273, "Victoria", 12],

    # Región de Los Ríos (13)
    [274, "Valdivia", 13],
    [275, "Corral", 13],
    [276, "Lanco", 13],
    [277, "Los Lagos", 13],
    [278, "Máfil", 13],
    [279, "Mariquina", 13],
    [280, "Paillaco", 13],
    [281, "Panguipulli", 13],
    [282, "La Unión", 13],
    [283, "Futrono", 13],
    [284, "Lago Ranco", 13],
    [285, "Río Bueno", 13],

    # Región de Los Lagos (14)
    [286, "Puerto Montt", 14],
    [287, "Calbuco", 14],
    [288, "Cochamó", 14],
    [289, "Fresia", 14],
    [290, "Frutillar", 14],
    [291, "Los Muermos", 14],
    [292, "Llanquihue", 14],
    [293, "Maullín", 14],
    [294, "Puerto Varas", 14],
    [295, "Castro", 14],
    [296, "Ancud", 14],
    [297, "Chonchi", 14],
    [298, "Curaco de Vélez", 14],
    [299, "Dalcahue", 14],
    [300, "Puqueldón", 14],
    [301, "Queilén", 14],
    [302, "Quellón", 14],
    [303, "Quemchi", 14],
    [304, "Quinchao", 14],
    [305, "Osorno", 14],
    [306, "Puerto Octay", 14],
    [307, "Purranque", 14],
    [308, "Puyehue", 14],
    [309, "Río Negro", 14],
    [310, "San Juan de la Costa", 14],
    [311, "San Pablo", 14],

    # Región de Aysén del General Carlos Ibáñez del Campo (15)
    [312, "Coyhaique", 15],
    [313, "Lago Verde", 15],
    [314, "Aysén", 15],
    [315, "Cisnes", 15],
    [316, "Guaitecas", 15],
    [317, "Cochrane", 15],
    [318, "O'Higgins", 15],
    [319, "Tortel", 15],
    [320, "Chile Chico", 15],
    [321, "Río Ibáñez", 15],

    # Región de Magallanes y de la Antártica Chilena (16)
    [322, "Punta Arenas", 16],
    [323, "Laguna Blanca", 16],
    [324, "Río Verde", 16],
    [325, "San Gregorio", 16],
    [326, "Cabo de Hornos", 16],
    [327, "Antártica", 16],
    [328, "Porvenir", 16],
    [329, "Primavera", 16],
    [330, "Timaukel", 16],
    [331, "Natales", 16],
    [332, "Torres del Paine", 16]
]
'''
# The list is now complete with all 374 communes of Chile along with their corresponding region numbers.


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