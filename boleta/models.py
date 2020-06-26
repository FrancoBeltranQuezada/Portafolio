from django.db import models

# Create your models here.
from django.db import models
from servicio.models import Servicio
from users.models import User
# Create your models here.


class Boleta (models.Model):
    id_boleta = models.IntegerField(primary_key=True)
    fecha = models.DateField()
    hora = models.TimeField()
    total = models.IntegerField()
    usuario_rut_usuario = models.ForeignKey(User, on_delete = models.SET_NULL, null = True)
    #forma_pago_id_forma_pago = models.ForeignKey('', on_delete = models.SET_NULL)
    #usuario_rol_id_rol = models.ForeignKey('', on_delete = models.SET_NULL)


class DetalleBoleta (models.Model):
    vunitario = models.IntegerField()
    desc_prod = models.CharField(max_length=30)
    cantidad = models.IntegerField(null=False)
    totallinea = models.IntegerField()
    boleta_id_boleta = models.ForeignKey(Boleta, on_delete = models.SET_NULL, null = True)
    servicio_id_servicio = models.ForeignKey(Servicio, on_delete = models.SET_NULL, null = True)




