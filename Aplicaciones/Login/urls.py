from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import CustomUser

# Create your views here.

def inicioSesion(request):
    if request.method == "POST":
        usuario = request.POST["usuario"]
        contrasena = request.POST["contrasena"]

        user = authenticate(request, username=usuario, password=contrasena)
        if user is not None:
            login(request, user)
            if user.role == "ADMIN":
                return redirect('inicioAdmin')
            else:
                return redirect('inicioUsuario')
        else:
            messages.error(request, "Usuario o contraseña incorrectos")
            return redirect('login')

    return render(request, "login/login.html")


def cerrarSesion(request):
    logout(request)
    return redirect('login')


def inicioAdmin(request):
    if not request.user.is_authenticated or request.user.role != "ADMIN":
        messages.error(request, "No tienes permiso para acceder a esta página")
        return redirect('login')
    return render(request, "login/inicioAdmin.html")


def inicioUsuario(request):
    if not request.user.is_authenticated:
        messages.error(request, "Inicia sesión primero")
        return redirect('login')
    return render(request, "login/inicioUsuario.html")
