from django.db import models
from users.models import User
from servicio.models import Servicio


class ModuloTiempo(models.Model):
    id_modulo = models.IntegerField(primary_key=True)
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()

    def __str__(self):
        a = str(self.hora_inicio) 
        b = str(self.hora_fin) 
        return a+" "+b
    

class Reserva(models.Model):
    id_reserva = models.IntegerField(primary_key=True)
    fecha = models.DateField()
    usuario = models.ForeignKey(User,null=True,blank=True,on_delete=models.CASCADE)
    patente = models.CharField(max_length=30,help_text="Ingrese Patente")
    marca = models.CharField(max_length=30,help_text="Ingrese marca")
    modelo = models.CharField(max_length=30,help_text="Ingrese modelo")
    modulo_tiempo = models.ForeignKey(ModuloTiempo,null=True,blank=True,on_delete=models.CASCADE)
    servicio = models.ForeignKey(Servicio,null=True,blank=True,on_delete=models.CASCADE)

    def __str__(self):
        a = str(self.id_reserva) 
        b =str(self.usuario)
        c = str(self.modulo_tiempo)
        return a +" "+ b +" " + c

