# -*- coding: utf-8 -*-

from django.contrib import admin
from apps.concesionarioapp.models import Categoria
from apps.concesionarioapp.models import DatosPersonales
from apps.concesionarioapp.models import Rol
from apps.concesionarioapp.models import UsuarioRol
from apps.concesionarioapp.models import Vehiculo

admin.site.register(Categoria)
admin.site.register(DatosPersonales)
admin.site.register(Rol)
admin.site.register(UsuarioRol)

class VehiculoAdmin(admin.ModelAdmin):
    list_display = ('vehplaca', 'datid', 'catid', 'vehmodelo', 'vehmarca', 'vehprecio')
    list_filter = ('vehplaca', 'vehmodelo', 'vehmarca')
    search_fields = ('vehplaca', 'vehmarca')
    ordering = ('vehmodelo',)

admin.site.register(Vehiculo, VehiculoAdmin)


