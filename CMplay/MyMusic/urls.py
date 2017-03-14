from django.conf.urls import url
from . import views

#namespace
app_name = 'MyMusic'

#url's registradas con sus respetivas vistas ,

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login_user/$', views.login_user, name='login_user'),
    url(r'^logout_user/$', views.logout_user, name='logout_user'),
    url(r'^cancionadd/$', views.nueva_cancion, name='cancion-add'),
    url(r'^listas/$', views.listas_view, name='listas'),
    url(r'^nueva_lista/$', views.nueva_lista, name='lista-add'),
    #direccion dinamica , depende de la id de la lista
    url(r'^(?P<lista_id>[0-9]+)/borrar_lista/$', views.borrar_lista, name='eliminar_lista'),
    url(r'^(?P<lista_id>[0-9]+)/datalles/$', views.detail_lista, name='lista_detallada'),
    url(r'^(?P<cancion_id>[0-9]+)/borrar_cancion/$', views.borar_cancion, name='eliminar_cancion'),
    url(r'^(?P<ratin>[0-9]+)/(?P<cancion_id>[0-9]+)/$', views.calificar, name='ratin_cancion'),
    url(r'^(?P<lista_id>[0-9]+)/borrar/(?P<cancion_id>[0-9]+)/$', views.borrar_cancio_lista, name='borrar_cancion_lista'),

    #en edicion

    url(r'^(?P<lista_id>[0-9]+)/$', views.editar_lista, name='editar_list'),

    #url(r'^(?P<ratin>[0-9]+)/(?P<cancion_act>[a-zA_Z]+)/$',views.calificar,name='ratin_cancion'),


]