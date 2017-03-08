from django import forms
from django.contrib.auth.models import User
from .models import Cancion, Lista

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class CancionForm(forms.ModelForm):

    class Meta:
        model = Cancion
        fields = ['titulo_cancion', 'artista',  'audio']


