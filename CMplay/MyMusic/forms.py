from django import forms
from django.contrib.auth.models import User
from .models import Cancion, Lista

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
    #canciones=forms.MultipleChoiceField(Cancion.objects.all())   #no funciona
    #canciones = forms.MultipleChoiceField( widget=forms.CheckboxSelectMultiple) ,widget=forms.SelectMultiple
    canciones=forms.ModelMultipleChoiceField(queryset=Cancion.objects.all())
    #canciones = forms.ModelMultipleChoiceField(queryset=Cancion.objects.all())

    class Meta:
        model = Lista
        fields = ['titulo_de_lista']

        """

    def __init__(self, *args, **kwargs):
        super(ChoiceForm, self).__init__(*args, **kwargs)
        self.fields['countries'] =  ModelChoiceField(queryset=YourModel.objects.all()),
                                             empty_label="Choose a countries",
        """