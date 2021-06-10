# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic.base import View
from django.contrib import auth
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from apps.concesionarioapp.models import UsuarioRol

# Create your views here.

class Login(View):

    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        username = request.POST.get("signin_username", "")
        password = request.POST.get("signin_password", "")
        usuario = auth.authenticate(username=username,
                                    password=password)
        if usuario != None and usuario.is_active:
            auth.login(request, usuario)
            lista_roles = UsuarioRol.objects.filter(usuid=usuario.pk)

            if len(lista_roles) > 0:
                if lista_roles[0].rolid.roltipo == "Vendedor":
                    return HttpResponseRedirect(reverse('vendedores:listar_vehiculos'))

                elif lista_roles[0].rolid.roltipo == "Comprador":
                    return HttpResponseRedirect(reverse('compradores:listar_vehiculos'))

                else:
                    messages.add_message(request, messages.ERROR, "Rol de usuario inexistente")

            else:
                messages.add_message(request, messages.ERROR, "El Usuario no tiene roles asignados")

        else:
            if usuario == None:
                messages.add_message(request, messages.ERROR, "El Usuario no existe en el Sistema")

            else:
                messages.add_message(request, messages.ERROR, "El Usuario esta inactivo")

        return render(request, 'login.html')

class Logout(View):
    def get(self, request):
        auth.logout(request)
        return HttpResponseRedirect(reverse('login'))
