from django.db import models
from django.contrib.auth.models import AbstractUser
from django.shortcuts import reverse


class User(AbstractUser):
    direccion =  models.CharField(max_length=50)
    telefono = models.CharField(max_length=50)
    rut = models.CharField(max_length=15)

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('user-detail', kwargs={'pk': self.pk})
    


    


    

