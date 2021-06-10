# -*- coding: utf-8 -*-
from django import forms
from django.utils.translation import ugettext_lazy as _
from apps.concesionarioapp.models import Vehiculo
from apps.concesionarioapp.models import DatosPersonales


class VehiculoForm(forms.ModelForm):
    class Meta:
        model = Vehiculo
        fields = "__all__"
        labels = {
            'vehplaca': _(u'Número de Placa:'),
            'catid': _(u'Categoría:'),
            'vehmodelo': _(u'Modelo:'),
            'vehmarca': _(u'Marca:'),
            'vehestado': _(u'Estado:'),
            'vehprecio': _(u'Precio:'),
            'vehfoto': _(u'Foto:'),
            'datid': _(u'')
        }

    def __init__(self, vendedor=None, *args, **kwargs):
        super(VehiculoForm, self).__init__(*args, **kwargs)

        if vendedor is not None:
            self.fields['datid'].widget = forms.HiddenInput()
            self.fields['datid'].initial = vendedor

        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})


class DatosPersonalesForm(forms.ModelForm):
    class Meta:
        model = DatosPersonales
        fields = "__all__"
        labels = {
            'datid': _(u'Id Usuario:'),
            'datnombre': _(u'Nombre del Usuario:'),
            'datapellido': _(u'Apellido del Usuario:'),
            'datipoid': _(u'Tipo del Documento:'),
            'datnumeroid': _(u'Número del Documento:'),
            'datelefono': _(u'Número de Teléfono:'),
            'datcorreo': _(u'Email del usuario:'),
            'foto': _(u'Foto del Usuario:'),
            'usuid': _(u'')
        }

    def __init__(self, usuario=None, *args, **kwargs):
        super(DatosPersonalesForm, self).__init__(*args, **kwargs)

        if usuario is not None:
            self.fields['usuid'].widget = forms.HiddenInput()
            self.fields['usuid'].initial = usuario

        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})
