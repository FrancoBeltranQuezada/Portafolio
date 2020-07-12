from django.db import models
from django.utils import timezone
# Create your models here.
from django.db import models
from servicio.models import Servicio
from producto.models import Producto
from users.models import User
from datetime import datetime
# Create your models here.


class Boleta (models.Model):
    id_boleta = models.IntegerField(primary_key=True, unique=True)
    fecha = models.DateField(default = datetime.now, verbose_name='Fecha de boleta')
    hora = models.TimeField()
    total = models.PositiveIntegerField()
    usuario = models.ForeignKey(User, on_delete = models.SET_NULL, null = True)
    #id_forma_pago = models.ForeignKey('', on_delete = models.SET_NULL)
    #id_rol = models.ForeignKey('', on_delete = models.SET_NULL)
    
    def __str__(self):
        return str(self.id_boleta)

    

    


class DetalleBoleta (models.Model):
    vunitario = models.PositiveIntegerField(verbose_name='Precio')
    desc_prod = models.CharField(max_length=30, verbose_name='Descripción producto')
    cantidad = models.PositiveIntegerField(null=False)
    totallinea = models.IntegerField()
    boleta_id_boleta = models.ForeignKey(Boleta, on_delete = models.SET_NULL, null = True)
    servicio = models.ForeignKey(Servicio, on_delete = models.SET_NULL, null = True)
    producto = models.ForeignKey(Producto, on_delete = models.CASCADE, null = True)


    def __str__(self):
        return self.boleta_id_boleta




