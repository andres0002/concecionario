from django.conf.urls import url
from apps.vendedores.views import ListadoVehiculos
from apps.vendedores.views import AdicionaVehiculo
from apps.vendedores.views import VisualizaVehiculo
from apps.vendedores.views import BorraVehiculo
from apps.vendedores.views import ModificaVehiculo
from apps.vendedores.views import ModificaPerfil

app_name = 'vendedores'

urlpatterns = [
    url(r'^listar-vehiculos/', ListadoVehiculos.as_view(), name='listar_vehiculos'),
    url(r'^adicionar-vehiculos/', AdicionaVehiculo.as_view(), name='adicionar_vehiculo'),
    url(r'^visualizar-vehiculos/(?P<id_vehiculo>\w+)', VisualizaVehiculo.as_view(), name='visualizar_vehiculo'),
    url(r'^borrar-vehiculos/(?P<id_vehiculo>\w+)', BorraVehiculo.as_view(), name='borrar_vehiculo'),
    url(r'^modificar-vehiculos/(?P<id_vehiculo>\w+)', ModificaVehiculo.as_view(), name='modificar_vehiculo'),
    url(r'^modificar-perfil/', ModificaPerfil.as_view(), name='modificar_perfil'),
]
