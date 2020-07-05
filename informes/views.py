from django.shortcuts import render
from django.http import JsonResponse
from django.db.models import Sum,Count    
from reserva.models import Reserva,Servicio

# Create your views here.


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