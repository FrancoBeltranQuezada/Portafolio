from django.shortcuts import render,redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Reserva
from .forms import ReservaForm
# Create your views here.

class CrearReserva(CreateView):
    model = ReservaForm
    form_class = ReservaForm
    success_url = "../gestion-reserva/"
    template_name = "reserva/reserva_create.html"
    

    #este metodo nos permite asignar el usuario que está actualmente logeado a nuestra reserva de manera automatica
    def form_valid(self, form):
        #Agrega el usuario logeado a la reserva asignando a la instancia de la reserva
        form.instance.usuario = self.request.user

        #llama al comportamiento form validation de la super-class
        return super(CrearReserva, self).form_valid(form)


class ListarReserva(ListView):
    model = Reserva
    template_name = 'reserva/reserva_list.html'
    context_object_name = 'reservas'
    ordering = ['-fecha']

class EliminarReserva(DeleteView):
    model = Reserva
    template_name = 'reserva/reserva_delete.html'
    success_url = '/reserva/gestion-reserva/'


def UpdateReservaView(request, pk):
    reserva = Reserva.objects.get(pk=pk)

    if request.method == 'POST':
        form = ReservaForm(data=request.POST, instance=reserva)
        if form.is_valid():
            form.save()
            print('si guardpo')
            return redirect('listar-reserva')
        else:
            print('no guardó')
    else:
        form = ReservaForm(instance=reserva)
    return render(request, 'reserva/reserva_form.html', {'form': form})
