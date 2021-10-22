from django.db import models
from apps.vehiculos.models import Vechiculo 

# Create your models here.
class Cliente (models.Model):
    nombre =models.CharField(max_length=50,verbose_name="nombre")
    cedula = models.IntegerField(verbose_name="cedula")
    fecha = models.DateField(verbose_name="fecha")
    vehiculo =models.ManyToManyField(Vechiculo,through="ClienteVehiculo")

    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name= "cliente"
        verbose_name_plural ="clientes"

class ClienteVehiculo (models.Model):
    cliente =models.ForeignKey(Cliente,on_delete= models.CASCADE, verbose_name="cliente")
    vehiculo =models.ForeignKey(Vechiculo,on_delete= models.CASCADE, verbose_name="vehiculo")
    total = models.IntegerField(verbose_name="total")
