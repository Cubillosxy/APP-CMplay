from django import forms
from django.contrib.auth.models import User
from .models import Cancion, Lista


#Formularios
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        labels={'username':'Nombre de Usuario','password':'contraseña'}

class CancionForm(forms.ModelForm):

    class Meta:
        model = Cancion
        fields = ['titulo_cancion', 'artista',  'audio']
        labels={'titulo_cancion':'Titulo de la Canción'}



class ListaForm(forms.ModelForm):

    #definimos un atributo de entrada extra , editando la clase
    def __init__(self,user, *args, **kwargs):
        super(ListaForm, self).__init__(*args, **kwargs)
        self.fields['canciones'] = forms.ModelMultipleChoiceField(queryset=Cancion.objects.filter(user=user)
                                                                  ,required=False,widget=forms.CheckboxSelectMultiple)
    class Meta:
        model = Lista
        fields = ['titulo_de_lista','canciones']

