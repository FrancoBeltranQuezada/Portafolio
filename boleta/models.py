from django.db import models

# Create your models here.
from django.db import models
from servicio.models import Servicio
from producto.models import Producto
from users.models import User
# Create your models here.


class Boleta (models.Model):
    id_boleta = models.IntegerField(primary_key=True)
    fecha = models.DateField(auto_now_add=True)
    hora = models.TimeField(auto_now_add=True)
    total = models.IntegerField()
    usuario = models.ForeignKey(User, on_delete = models.SET_NULL, null = True)
    #id_forma_pago = models.ForeignKey('', on_delete = models.SET_NULL)
    #id_rol = models.ForeignKey('', on_delete = models.SET_NULL)

    

    


class DetalleBoleta (models.Model):
    vunitario = models.IntegerField()
    desc_prod = models.CharField(max_length=30, help_text="Ingrese descuento")
    cantidad = models.IntegerField(null=False)
    totallinea = models.IntegerField()
    boleta_id_boleta = models.ForeignKey(Boleta, on_delete = models.SET_NULL, null = True)
    servicio = models.ForeignKey(Servicio, on_delete = models.SET_NULL, null = True)
    producto = models.ForeignKey(Producto, on_delete = models.CASCADE, null = True)




