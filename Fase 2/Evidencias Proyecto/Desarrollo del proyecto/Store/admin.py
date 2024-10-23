from django.contrib import admin
from .models import (
    Usuario, Proveedor, TipoProducto, Categoria, Subcategoria, Marca, Producto, 
    Valoracion, Orden, Ordenxproducto, MensajeOrden
)

# Registrando todos los modelos en el admin
@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('username', 'RUT', 'genero', 'telefono', 'direccion', 'region', 'comuna')

@admin.register(Proveedor)
class ProveedorAdmin(admin.ModelAdmin):
    list_display = ('nombreproveedor', 'direccion', 'telefono', 'email', 'fecha_registro')

@admin.register(TipoProducto)
class TipoProductoAdmin(admin.ModelAdmin):
    list_display = ('nombretipo', 'id_tipo')

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombrecategoria', 'tipo_producto', 'id_categoria')

@admin.register(Subcategoria)
class SubcategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre_subcategoria', 'categoria', 'id_subcategoria')

@admin.register(Marca)
class MarcaAdmin(admin.ModelAdmin):
    list_display = ('nombre_marca', 'id_marca')

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre_producto', 'SKU', 'Precio_compra', 'precio_venta', 'stock', 'marca', 'proveedor')

@admin.register(Valoracion)
class ValoracionAdmin(admin.ModelAdmin):
    list_display = ('usuario_validacion', 'producto_valorado', 'cantidad_estrellas', 'desc_valoracion')

@admin.register(Orden)
class OrdenAdmin(admin.ModelAdmin):
    list_display = ('id_orden', 'usuario_rel', 'direccion_entrega', 'estado', 'fecha_creacion')

@admin.register(Ordenxproducto)
class OrdenxproductoAdmin(admin.ModelAdmin):
    list_display = ('id_orden_relacion', 'id_producto', 'cantidad_producto', 'valorado')

@admin.register(MensajeOrden)
class MensajeOrdenAdmin(admin.ModelAdmin):
    list_display = ('id_mensaje', 'titulo_mensaje', 'fecha_creacion', 'id_orden_asociada', 'id_usuario_creador')