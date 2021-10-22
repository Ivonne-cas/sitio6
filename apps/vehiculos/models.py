from django.db import models

# Create your models here.
class Vechiculo (models.Model):
    marca=models.CharField(max_length=50,verbose_name="marca")
    fecha=models.DateField(verbose_name="fecha")
    descripcion=models.CharField(max_length=100,verbose_name="descripcion")
    compro = models.BooleanField(verbose_name="compro")

    def __str__(self):
        return self.marca
    
    class Meta:
        verbose_name ="vehiculo"
        verbose_name_plural ="vehiculos"