from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
#rut,telefono,direccion

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    direccion =  models.CharField(max_length=50)
    telefono = models.CharField(max_length=50)
    rut = models.CharField(max_length=15)

    def __str__(self):
        return f'{self.user.username} Perfil'

    def get_absolute_url(self):
        return reverse('user-detail', kwargs={'pk': self.pk})
    

