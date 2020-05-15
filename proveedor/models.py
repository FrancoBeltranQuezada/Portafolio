from django.db import models

# Create your models here.

class prov(models.Model):
    id_prov = models.AutoField(primary_key=True)
    nombre_proveedor= models.CharField(max_length=30)
    
