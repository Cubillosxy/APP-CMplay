from django.db import models
from django.contrib.auth.models import Permission, User

# Create your models here.

class Cancion(models.Model):
    user = models.ForeignKey(User, default=1)
    titulo_cancion=models.CharField(max_length=500)
    artista = models.CharField(max_length=250)
    audio = models.FileField(default='')

    def __str__(self):
        return self.titulo_cancion

class Lista(models.Model):
    user_l = models.ForeignKey(User, default=1)
    titulo_lista=models.CharField(max_length=500)
    artista = models.CharField(max_length=250)
    cancion = models.ManyToManyField(Cancion,default=None)


    def __str__(self):
        return self.titulo_lista