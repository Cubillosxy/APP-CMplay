from django.db import models
from django.contrib.auth.models import Permission, User

# Create your models here.

class Cancion(models.Model):
    #muchas canciones pueden pertenecer a un usuario ManyToOne
    user = models.ForeignKey(User, default=1)
    titulo_cancion=models.CharField(max_length=500)
    artista = models.CharField(max_length=250)
    audio = models.FileField(default='')

    def __str__(self):
        return self.titulo_cancion

class Lista(models.Model):
    user_list = models.ForeignKey(User, default=User)
    titulo_de_lista=models.CharField(max_length=500)

    #un lista puede tener muchas canciones, y una canciones puede pertenecer a varias listas
    canciones = models.ManyToManyField(Cancion,blank=True)

    def __str__(self):
        return self.titulo_de_lista

class Calificacion(models.Model):
    user_calificador=models.CharField(max_length=30)
    rating=models.IntegerField(default=0)
    rating_s=models.CharField(max_length=6)
    fue_calificado=models.BooleanField(default=False)
    #una canción puede tener muchas calificaciones
    cancion_calificada=models.ForeignKey(Cancion)

    def __int__(self):
        return self.rating


