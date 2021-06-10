# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.generic.base import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

from apps.concesionarioapp.models import DatosPersonales
from apps.concesionarioapp.models import Vehiculo

from apps.concesionarioapp.forms import VehiculoForm
from apps.concesionarioapp.forms import DatosPersonalesForm


class ListadoVehiculos(LoginRequiredMixin, View):
    login_url = '/'
    template_name = 'compradores/listar_vehiculos.html'

    def get(self, request):
        try:
            datos_usuario = DatosPersonales.objects.get(usuid=request.user.pk)
            lista_vehiculos = Vehiculo.objects.all()
            return render(request,
                          self.template_name,
                          {'vehiculos': lista_vehiculos,
                           'foto_usuario': datos_usuario.foto})

        except DatosPersonales.DoesNotExist:
            return render(request, "pages-404.html")


class ModificaPerfil(LoginRequiredMixin, View):
    login_url = '/'
    form_class = DatosPersonalesForm
    template_name = 'compradores/perfil_comprador.html'

    def get(self, request):
        try:
            datos_usuario = DatosPersonales.objects.get(usuid=request.user.pk)
            form = self.form_class(request.user, instance=datos_usuario)
            return render(request,
                          self.template_name,
                          {'form': form,
                           'foto_usuario': datos_usuario.foto})

        except DatosPersonales.DoesNotExist:
            return render(request, "pages-404.html")

    def post(self, request):
        try:
            datos_usuario = DatosPersonales.objects.get(usuid=request.user.pk)
            form = self.form_class(request.user, request.POST, request.FILES, instance=datos_usuario)

            if form.is_valid():
                form.save()
                messages.add_message(request, messages.INFO, 'El Perfil se modificó correctamente')

            else:
                messages.add_message(request, messages.ERROR, 'El Perfil no se pudo modificar')

            return self.get(request)

        except DatosPersonales.DoesNotExist:
            return render(request, "pages-404.html")


class VisualizaPerfilVendedor(LoginRequiredMixin, View):
    login_url = '/'
    form_class = DatosPersonalesForm
    template_name = 'compradores/perfil_vendedor.html'

    def get(self, request, id_vendedor):
        try:
            datos_usuario = DatosPersonales.objects.get(usuid=id_vendedor)
            form = self.form_class(request.user, instance=datos_usuario)
            return render(request,
                          self.template_name,
                          {'form': form,
                           'foto_usuario': datos_usuario.foto})

        except DatosPersonales.DoesNotExist:
            return render(request, "pages-404.html")


class VisualizaVehiculo(LoginRequiredMixin, View):
    login_url = '/'
    form_class = VehiculoForm
    template_name = 'compradores/visualizar_vehiculo.html'

    def get(self, request, id_vehiculo):
        try:
            datos_usuario = DatosPersonales.objects.get(usuid=request.user.pk)
            vehiculo = Vehiculo.objects.get(vehplaca=id_vehiculo)
            form = self.form_class(datos_usuario, instance=vehiculo)
            return render(request,
                          self.template_name,
                          {'form': form,
                           'foto_vehiculo': vehiculo.vehfoto,
                           'foto_usuario': datos_usuario.foto})

        except DatosPersonales.DoesNotExist:
            return render(request, "pages-404.html")

        except Vehiculo.DoesNotExist:
            return render(request, "pages-404.html")