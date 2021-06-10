from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from django.conf import settings

from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from apps.concesionarioapp.views import Login
from apps.concesionarioapp.views import Logout

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', Login.as_view(), name='login'),
    url(r'^logout/', Logout.as_view(), name='logout'),
    url(r'^vendedores/', include('apps.vendedores.urls', namespace='vendedores')),
    url(r'^compradores/', include('apps.compradores.urls', namespace='compradores')),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
