from django.db import models

# Create your models here.

class prov(models.Model):
    id_prov = models.AutoField(primary_key=True)
    nombre_proveedor= models.CharField(max_length=30, help_text="Ingrese nombre proveedor")
    def __str__(self):
        return self.nombre_proveedor
    class Meta:
        ordering = ['nombre_proveedor']
    
