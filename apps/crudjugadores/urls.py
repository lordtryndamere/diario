from django.conf.urls import url
from apps.crudjugadores.views import JugadorCreate, JugadorList, JugadorDelete, JugadorUpdate, JugadorShow, search

urlpatterns = [
    url(r'^nuevo/', JugadorCreate.as_view(), name='jugador_crear'),
    url(r'^listar', JugadorList.as_view(), name='jugador_listar'),
    url(r'^eliminar/(?P<pk>\d+)/$', JugadorDelete.as_view(), name='jugador_eliminar'),
    url(r'^editar/(?P<pk>\d+)/$', JugadorUpdate.as_view(), name='jugador_editar'),
    url(r'^mostrar/(?P<pk>\d+)/$', JugadorShow.as_view(), name='jugador_mostrar'),
    url(r'^buscar/$', search, name='jugador_buscar'),
]