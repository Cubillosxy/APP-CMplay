from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import JsonResponse
from django.db.models import Q
from django.shortcuts import render,get_object_or_404,redirect
from .forms import UserForm,CancionForm,ListaForm
from .models import Cancion,Lista,Calificacion

#extensiones permitidas para archivos de audio
AUDIO_EXT = ['wav', 'mp3']


#vista de formulario añadir
def nueva_cancion(request):
    if not request.user.is_authenticated():
        return render(request, 'MyMusic/login_form.html')
    else:
        form = CancionForm(request.POST or None, request.FILES or None)

        if form.is_valid():
            cancion = form.save(commit=False)
            cancion.user = request.user

            cancion.audio = request.FILES['audio']

            #recuperamos el archivo y guardamos su extensión
            file_type = cancion.audio.url.split('.')[-1]
            file_type = file_type.lower()
            canciones = Cancion.objects.filter(user=request.user)

            if file_type not in AUDIO_EXT:
                context = {
                    'form': form,
                    'error_message': 'El archivo debe ser MP3 o WAV',
                }
                #enviamos de vuelta a la pagina
                return render(request, 'MyMusic/cancion_form.html', context)
            cancion.save()
            context = {
                'canciones': canciones,
                'username': request.user.username
            }
            return render(request, 'MyMusic/index.html', context)
        context = {
            "form": form,
            'error_message': 'Error en Formulario',
        }
        return render(request, 'MyMusic/cancion_form.html', context)

#vista nueva lista
def nueva_lista(request):
    #form=ListaForm(request.POST or None, request.FILES or None)
    form = ListaForm(request.user,request.POST or None, request.FILES or None)



    if form.is_valid():
        lista = form.save(commit=False)
        lista.user_list = request.user
        lista.save()

        lista.canciones = form.cleaned_data['canciones']


        context = {
            'username': request.user.username,
            'lista': lista,
        }
        #return render(request,'MyMusic/lista_detail.html',context)
        return redirect('/')
    context={
        'form':form,
        'error_message': 'Error ',
    }
    return render(request,'MyMusic/lista_form.html',context)

def listas_view(request):
    canciones_user = Cancion.objects.filter(user=request.user)
    listas_user=Lista.objects.filter(user_list=request.user)
    context = {
        'canciones': canciones_user,
        'username': request.user.username,
        'listas':listas_user,
    }
    return render(request, 'MyMusic/listas.html', context)



# Create your views here.
def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'MyMusic/login_form.html', context)


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                canciones = Cancion.objects.filter(user=request.user)
                context={
                    'canciones': canciones,
                     'username': username
                         }
                return render(request, 'MyMusic/index.html',context )
            else:
                return render(request, 'MyMusic/login_form.html', {'error_message': 'Su cuenta ha sido deshabilitada'})
        else:
            return render(request, 'MyMusic/login_form.html', {'error_message': 'El usuario no existe'})
    return render(request, 'MyMusic/login_form.html')


def register(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                canciones = Cancion.objects.filter(user=request.user)
                context={
                    'canciones': canciones,
                     'username': username
                         }
                return render(request, 'MyMusic/index.html', context)
    context = {
        "form": form,
    }
    return render(request, 'MyMusic/registration_form.html', context)

def index(request):
    if not request.user.is_authenticated():
        return render(request, 'MyMusic/login_form.html')
    else:
        #canciones = Cancion.objects.filter(user=request.user)
        canciones=Cancion.objects.all()
        canciones_user=Cancion.objects.filter(user=request.user)

        #song_results = Song.objects.all()
        query = request.GET.get("q")
        if query:
            canciones = canciones.filter(Q(titulo_cancion__icontains=query) |  Q(artista__icontains=query)).distinct()
            """
            song_results = song_results.filter(
                Q(song_title__icontains=query)
            ).distinct()
            """
            return render(request, 'MyMusic/index.html', {
                'canciones': canciones,
                'username': request.user.username,
            })
        else:
            return render(request, 'MyMusic/index.html', {'canciones': canciones_user, 'username': request.user.username})

def calificar(request,ratin, cancion_act):
    try:
        #cancion=get_object_or_404(Cancion, pk=cancion.pk)  #recuperamos la cancion indicada
        cancion=Cancion.get(pk=cancion_act.pk)
        # obtenemos todas las calificaciones de la canción
        calificaciones=cancion.calificacion_set.all()

        #buscamos si la cancion fue calificada por este usuario
        for cancion_cal in calificaciones:
            if cancion_cal.user_calificador==request.user.username:
                print ("la cancion ya fue calificada")
                context={}
                return JsonResponse({'success': False})
        calificacion = Calificacion(user_calificador=request.user.username, rating=ratin, fue_calificado=True,
                                    cancion_calificada=cancion)
        calificacion.save()
        print ("Se califico")
        context={}
        return JsonResponse({'success': True})
    except :
        return JsonResponse({'success': False})
        print ("No se califico")

"""
    else:
        calificacion=Calificacion(user_calificador=request.user.username,rating=ratin,
                                  fue_calificado=True,cancion_calificada=cancion)
        calificacion.save()
"""

def detail(request):
    pass