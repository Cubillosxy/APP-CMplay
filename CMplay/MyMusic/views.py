from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.db.models import Q
from django.shortcuts import render,get_object_or_404
from .forms import UserForm
from .models import Cancion,Lista


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
                return render(request, 'MyMusic/index.html', {'canciones': canciones})
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
                return render(request, 'MyMusic/index.html', {'canciones': canciones})
    context = {
        "form": form,
    }
    return render(request, 'MyMusic/registration_form.html', context)

def index(request):
    if not request.user.is_authenticated():
        return render(request, 'MyMusic/login_form.html')
    else:
        canciones = Cancion.objects.filter(user=request.user)
        #song_results = Song.objects.all()
        query = request.GET.get("q")
        if query:
            canciones = canciones.filter(
                Q(album_title__icontains=query) |
                Q(artist__icontains=query)
            ).distinct()
            """
            song_results = song_results.filter(
                Q(song_title__icontains=query)
            ).distinct()
            """
            return render(request, 'MyMusic/index.html', {
                'canciones': canciones,
                #songs': song_results,
            })
        else:
            return render(request, 'MyMusic/index.html', {'canciones': canciones})

