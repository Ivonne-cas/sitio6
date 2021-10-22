from django.contrib import admin
from django.contrib.admin.options import ModelAdmin, TabularInline
from django.db import models
from apps.clientes.models import Cliente,ClienteVehiculo
# Register your models here.
class MembershipInline(admin.TabularInline):
    model = ClienteVehiculo
    extra = 1 

class ClienteAdmin(admin.ModelAdmin):
    inlines = (MembershipInline,)
    list_display =('nombre','cedula','fecha')
    ordering = ('nombre','cedula','fecha')
    search_fields =('nombre','cedula')

admin.site.register(Cliente,ClienteAdmin)