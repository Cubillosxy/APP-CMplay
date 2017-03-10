from django.conf.urls import url
from . import views

app_name = 'MyMusic'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login_user/$', views.login_user, name='login_user'),
    url(r'^logout_user/$', views.logout_user, name='logout_user'),
    url(r'^cancionadd/$', views.nueva_cancion, name='cancion-add'),
    url(r'^listas/$', views.listas_view, name='listas'),
    url(r'^nueva_lista/$', views.nueva_lista, name='lista-add'),


    url(r'^(?P<user_id>[0-9]+)/$', views.detail, name='detail'),
]