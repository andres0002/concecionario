from django.conf.urls import url
from apps.compradores.views import ListadoVehiculos
from apps.compradores.views import ModificaPerfil
from apps.compradores.views import VisualizaPerfilVendedor
from apps.compradores.views import VisualizaVehiculo

app_name = 'compradores'

urlpatterns = [
    url(r'^listar-vehiculos/', ListadoVehiculos.as_view(), name='listar_vehiculos'),
    url(r'^modificar-perfil/', ModificaPerfil.as_view(), name='modificar_perfil'),
    url(r'^perfil-vendedor/(?P<id_vendedor>\w+)', VisualizaPerfilVendedor.as_view(), name='visualizar_perfil_vendedor'),
    url(r'^visualizar-vehiculos/(?P<id_vehiculo>\w+)', VisualizaVehiculo.as_view(), name='visualizar_vehiculo'),
]
