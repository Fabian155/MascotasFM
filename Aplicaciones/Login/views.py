from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import CustomUser
from django.contrib.auth.decorators import login_required

# Create your views here.

def inicioSesion(request):
    if request.method == "POST":
        usuario = request.POST["usuario"]
        contrasena = request.POST["contrasena"]

        user = authenticate(request, username=usuario, password=contrasena)
        if user is not None:
            login(request, user)
            if user.is_superuser or user.role == "ADMIN":
                return redirect('inicioAdmin')
            else:
                return redirect('inicioUsuario')
        else:
            messages.error(request, "Usuario o contraseña incorrectos")
            return redirect('login')

    return render(request, "login.html")


def cerrarSesion(request):
    logout(request)
    return redirect('login')


def inicioAdmin(request):
    if not request.user.is_authenticated or request.user.role != "ADMIN":
        messages.error(request, "No tienes permiso para acceder a esta página")
        return redirect('inicioUsuario')
    return render(request, "inicioAdmin.html")


# 👤 VISTA PARA USUARIO
@login_required(login_url='login')
def inicioUsuario(request):
    if not request.user.is_authenticated:
        messages.error(request, "Inicia sesión primero")
        return redirect('login')
    if request.user.role == "ADMIN":
        return redirect('inicioAdmin')
    return render(request, "inicioUsuario.html")
