# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.contrib.auth.models import User

class Categoria(models.Model):
    catid = models.AutoField(primary_key=True)
    catipo = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):# unicode
        return self.catipo

    class Meta:
        verbose_name_plural = "Categorias"
        verbose_name = "Categoria"

DOC_CHOICES = (
    ('CC', _(u"Cédula de Ciudadanía (CC)")),
    ('TI', _(u"Tarjeta de Identidad (TI)")),
    ('RC', _(u"Registro Civil (RC)")),
    ('CE', _(u"Cédula de Extranjería (CE)")),
    ('CI', _(u"Carné de Identidad (CI)")),
    ('DNI', _(u"Documento Nacional de Identidad (DNI)")),
    ('DUI', _(u"Documento Único de Identidad (DUI)"))
)

class DatosPersonales(models.Model):
    datid = models.AutoField(primary_key=True)
    datnombre = models.CharField(max_length=50)
    datapellido = models.CharField(max_length=50, blank=True, null=True)
    datipoid = models.CharField(max_length=20, blank=True, null=True, choices=DOC_CHOICES, default='CC')
    datnumeroid = models.CharField(max_length=20, blank=True, null=True)
    datelefono = models.CharField(max_length=20, blank=True, null=True)
    datcorreo = models.CharField(max_length=50, blank=True, null=True)
    foto = models.ImageField(upload_to='usuarios', default='usuarios/usuario.png')
    usuid = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):# unicode
        return "%s %s" % (self.datnombre, self.datapellido)

    class Meta:
        verbose_name_plural = "Datos Personales"
        verbose_name = "Datos Persona"

class Rol(models.Model):
    rolid = models.AutoField(primary_key=True)
    roltipo = models.CharField(max_length=50)

    def __str__(self):# unicode
        return self.roltipo

    class Meta:
        verbose_name_plural = "Roles"
        verbose_name = "Rol"

class UsuarioRol(models.Model):
    rolid = models.ForeignKey(Rol, on_delete=models.CASCADE)
    usuid = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):# unicode
        return "%s-%s" % (self.rolid.roltipo, self.usuid.username)

    class Meta:
        verbose_name_plural = "Roles Usuarios"
        verbose_name = "Rol Usuario"

class Vehiculo(models.Model):
    vehplaca = models.CharField(primary_key=True, max_length=10)
    catid = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    vehmodelo = models.IntegerField()
    vehmarca = models.CharField(max_length=50)
    vehestado = models.CharField(max_length=30, blank=True, null=True)
    vehprecio = models.IntegerField()
    vehfoto = models.ImageField(upload_to='vehiculos', default='vehiculos/vehiculo.png')
    datid = models.ForeignKey(DatosPersonales, on_delete=models.CASCADE)

    def __str__(self):# unicode
        return "%s-%s" % (self.vehplaca, self.vehmarca)

    class Meta:
        verbose_name_plural = "Vehiculos"
        verbose_name = "Vehiculo"
