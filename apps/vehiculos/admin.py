from django.contrib import admin
from apps.vehiculos.models import Vechiculo
# Register your models here.

class VehiculoAdmin(admin.ModelAdmin):
    list_display =('marca','fecha','descripcion','compro')
    ordering =('marca','fecha','descripcion','compro')
    search_fields =('marca','descripcion')

admin.site.register(Vechiculo,VehiculoAdmin)