from django.db import models
from users.models import User
from servicio.models import Servicio
import datetime
from django.core.exceptions import ValidationError


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

    def clean(self, *args, **kwargs):
       # qs= Reserva.objects.values('fecha').filter(fecha='2020-07-31').filter(modulo_tiempo_id = 2)

       #queryset que nos trae la cantidad de reservas en la fecha y modulo de tiempo seleccionado
        qs= Reserva.objects.values('fecha').filter(fecha=self.fecha).filter(modulo_tiempo_id = self.modulo_tiempo)


        #Se valida que la fecha no sea menor a hoy
        if self.fecha < datetime.date.today() or qs.count()>=2 :
            #Se eleva un mensaje de error
            if self.fecha < datetime.date.today():

                raise ValidationError("Error, La fecha no puede ser inferior a Hoy")
                #Se valida que la queryset no tenga mas de 2 reservas en la fecha y horario seleccionado
            elif qs.count()>=2:
                raise ValidationError("Error, Reservas para el modulo agotado")
        super(Reserva, self)
        

    def __str__(self):
        a = str(self.id_reserva) 
        b =str(self.usuario)
        c = str(self.modulo_tiempo)
        return a +" "+ b +" " + c

