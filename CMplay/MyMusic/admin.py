from django.contrib import admin
from .models import Cancion,Lista

# Register your models here.
#registramos para ver en admin
admin.site.register(Cancion)
admin.site.register(Lista)