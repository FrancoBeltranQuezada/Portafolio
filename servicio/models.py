from django.db import models

# Create your models here.


class Servicio (models.Model):
    id_servicio = models.IntegerField(primary_key=True , max_length=15)
    nombre_servicio = models.CharField(max_length=20 , help_text="Ingrese nombre de servicio")
    valor_servicio = models.IntegerField(null=False)   
    id_estado_servicio = models.ForeignKey('EstadoServicio', on_delete = models.SET_NULL, null= True) 



class EstadoServicio (models.Model):
    id_estado_servicio = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=30 , help_text="Ingrese descripcion")