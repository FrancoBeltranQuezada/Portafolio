from django.shortcuts import render
from django.http import JsonResponse
from django.db.models import Sum,Count    
from reserva.models import Reserva,Servicio
import datetime
from django import template



# Create your views here.{}
def informes_view(request):
    
    return render(request, 'informes/informes.html')




def reservas_pie(request):
    labels=[]
    data =[]

    queryset = Reserva.objects.values('servicio__nombre_servicio').annotate(count_servicio=Count('servicio')).order_by('count_servicio')
    for reserva in queryset:
        labels.append(reserva['servicio__nombre_servicio'])
        data.append(reserva['count_servicio'])

    return JsonResponse(data={
        'labels': labels,
        'data': data,
    })

    #queryset para obtener la fecha de las reservas
   # query= Reserva.objects.values('fecha').filter(fecha=datetime.datetime.today()).filter(modulo_tiempo_id = 2) 
                                                  #aqui va el filtro de la fecha
    #con esta query se filtra por modulo de hora
    #query= Reserva.objects.values('modulo_tiempo_id')
    #query con filtro fecha y modulo tiempo
    #query= Reserva.objects.values('fecha').filter(fecha='2020-07-19').filter(modulo_tiempo_id = 2)

    # query= Reserva.objects.values('fecha').filter(fecha=datetime.datetime.today() + datetime.timedelta(days=1))
    # datetime.date.today() + datetime.timedelta(days=1)