from django.db import models

# Create your models here.

#clase Producto almacenará todos los datos respectivos de Productos del sistema(ejemplo: aceite,llave 14", etc)
class Producto (models.Model):
    id_producto = models.CharField(primary_key=True , max_length=15)
    descripcion = models.CharField(max_length=20,help_text="Ingrese el nombre del producto")
    valor_compra = models.IntegerField(null=False)
    valor_venta = models.IntegerField(null=False)
    stock = models.IntegerField(null=False)
    stock_critico = models.IntegerField(null=False)
    id_estado_producto = models.ForeignKey('EstadoProducto', on_delete = models.SET_NULL, null=True)


    def __str__(self):
        return self.descripcion
    
class EstadoProducto (models.Model):
    id_estado_producto = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=30, help_text="Ingrese estado del producto")


    def __str__(self):
        return self.descripcion