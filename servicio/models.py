from django.db import models

# Create your models here.


class Servicio (models.Model):
    id_servicio = models.IntegerField(primary_key=True)
    nombre_servicio = models.CharField(max_length=50 , help_text="Ingrese nombre de servicio", unique=True, null=False)
    valor_servicio = models.IntegerField(null=False)   
    id_estado_servicio = models.ForeignKey('EstadoServicio', on_delete = models.SET_NULL, null= True) 

    def __str__(self):
        return self.nombre_servicio
    


class EstadoServicio (models.Model):
    id_estado_servicio = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=30 , help_text="Ingrese Descripción")


    def __str__(self):
        return self.descripcion