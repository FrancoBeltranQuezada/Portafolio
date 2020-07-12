from django import template
import datetime
register = template.Library()

from reserva.models import Reserva

@register.simple_tag
def total_reservas():
    qs= Reserva.objects.values()
    return qs.count()



@register.inclusion_tag('informes/mañana.html')
def show_reservas_mañana():
    reserv= Reserva.objects.all().values('id_reserva','fecha','patente','marca','modelo','servicio__nombre_servicio','usuario__first_name','modulo_tiempo_id__hora_inicio','modulo_tiempo_id__hora_fin','modulo_tiempo_id__hora_inicio',).filter(fecha=datetime.datetime.today() + datetime.timedelta(days=1))   

    return {'reserv':reserv}


@register.inclusion_tag('informes/hoy.html')
def show_reservas_hoy():
    reserv= Reserva.objects.all().values('id_reserva','fecha','patente','marca','modelo','servicio__nombre_servicio','usuario__first_name','modulo_tiempo_id__hora_inicio','modulo_tiempo_id__hora_fin','modulo_tiempo_id__hora_inicio',).filter(fecha=datetime.datetime.today())   

    return {'reserv':reserv}
