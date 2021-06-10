# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic.base import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

from apps.concesionarioapp.models import DatosPersonales
from apps.concesionarioapp.models import Vehiculo

from apps.concesionarioapp.forms import VehiculoForm
from apps.concesionarioapp.forms import DatosPersonalesForm


# Create your views here.

class ListadoVehiculos(LoginRequiredMixin, View):
    login_url = '/'
    template_name = 'vendedores/listar_vehiculos.html'

    def get(self, request):
        try:
            datos_usuario = DatosPersonales.objects.get(usuid=request.user.pk)
            lista_vehiculos = Vehiculo.objects.filter(datid=datos_usuario.pk)
            return render(request,
                          self.template_name,
                          {'vehiculos': lista_vehiculos,
                           'foto_usuario': datos_usuario.foto})

        except DatosPersonales.DoesNotExist:
            return render(request, "pages-404.html")


class AdicionaVehiculo(LoginRequiredMixin, View):
    login_url = '/'
    form_class = VehiculoForm
    template_name = 'vendedores/adicionar_vehiculo.html'

    def get(self, request):
        try:
            datos_usuario = DatosPersonales.objects.get(usuid=request.user.pk)
            form = self.form_class(datos_usuario)
            return render(request,
                          self.template_name,
                          {'form': form,
                           'foto_vehiculo': None,
                           'foto_usuario': datos_usuario.foto})

        except DatosPersonales.DoesNotExist:
            return render(request, "pages-404.html")

    def post(self, request):
        try:
            datos_usuario = DatosPersonales.objects.get(usuid=request.user.pk)
            form = self.form_class(datos_usuario, request.POST, request.FILES)

            if form.is_valid():
                form.save()
                messages.add_message(request, messages.INFO, 'El Vehículo se adicionó correctamente')

            else:
                messages.add_message(request, messages.ERROR, 'El Vehículo no se pudo adicionar')

            listar = ListadoVehiculos()
            return listar.get(request)

        except DatosPersonales.DoesNotExist:
            return render(request, "pages-404.html")


class VisualizaVehiculo(LoginRequiredMixin, View):
    login_url = '/'
    form_class = VehiculoForm
    template_name = 'vendedores/visualizar_vehiculo.html'

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


class BorraVehiculo(LoginRequiredMixin, View):
    login_url = '/'
    form_class = VehiculoForm
    template_name = 'vendedores/borrar_vehiculo.html'

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

    def post(self, request, id_vehiculo):
        try:
            vehiculo = Vehiculo.objects.get(vehplaca=id_vehiculo)
            vehiculo.delete()
            messages.add_message(request, messages.INFO, "El Vehículo se borró correctamente")
            listar = ListadoVehiculos()
            return listar.get(request)

        except Vehiculo.DoesNotExist:
            return render(request, "pages-404.html")


class ModificaVehiculo(LoginRequiredMixin, View):
    login_url = '/'
    form_class = VehiculoForm
    template_name = 'vendedores/modificar_vehiculo.html'

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

    def post(self, request, id_vehiculo):
        try:
            datos_usuario = DatosPersonales.objects.get(usuid=request.user.pk)
            vehiculo = Vehiculo.objects.get(vehplaca=id_vehiculo)
            form = self.form_class(datos_usuario, request.POST, request.FILES, instance=vehiculo)

            if form.is_valid():
                form.save()
                messages.add_message(request, messages.INFO, 'El Vehículo se modificó correctamente')

            else:
                messages.add_message(request, messages.ERROR, 'El Vehículo no se pudo modificar')

            listar = ListadoVehiculos()
            return listar.get(request)

        except DatosPersonales.DoesNotExist:
            return render(request, "pages-404.html")

        except Vehiculo.DoesNotExist:
            return render(request, "pages-404.html")


class ModificaPerfil(LoginRequiredMixin, View):
    login_url = '/'
    form_class = DatosPersonalesForm
    template_name = 'vendedores/perfil_vendedor.html'

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