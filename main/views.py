from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import *
from django.contrib.auth.models import User

def Logout(request):
    logout(request)
    return redirect("/accounts/login/")

def login_page(request):
    message=None
    if 'ava' in request.session:
        return redirect("/")
    else:
        if request.method=="POST":
            form = LoginForm(request.POST)
            if form.is_valid():
                username = request.POST['username']
                password = request.POST['password']
                user = authenticate(username=username, password=password)
                if user is not None:
                    if user.is_active:
                        login(request, user)
                        usuario = User.objects.get(username__exact=username)
                        request.session["ID"] = usuario.pk
                        request.session["ava"] = usuario.avatar.Imagen.url
                        return redirect("/")
                    else:
                        message ="Usuario no esta activo contacta al admin"
                else:
                    message = "Nombre de usuario y/o Contrasena no valido"
        else:
            form = LoginForm()
        return render(request, 'login.html', {'message': message, 'form': form})
