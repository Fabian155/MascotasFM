from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.hashers import make_password, check_password
from .models import Registrar  # 🔹 nuevo modelo de usuarios registrados


def inicioSesion(request):
    if request.method == "POST":
        correo = request.POST.get("usuario")
        clave = request.POST.get("contrasena")

        try:
            usuario = Registrar.objects.get(correo=correo)

            # Verificamos la contraseña hasheada
            if check_password(clave, usuario.contraseña):
                # Guardamos los datos en la sesión manualmente
                request.session["usuario_id"] = usuario.id
                request.session["usuario_nombre"] = usuario.nombre
                request.session["usuario_correo"] = usuario.correo
                messages.success(request, f"Bienvenido, {usuario.nombre} 👋")
                return redirect("inicioUsuario")

            else:
                messages.error(request, "Contraseña incorrecta. Intenta de nuevo.")
        except Registrar.DoesNotExist:
            messages.error(request, "El correo ingresado no existe. Regístrate primero.")

    return render(request, "login.html")



def cerrarSesion(request):
    logout(request)

    request.session.flush()
    messages.info(request, "Sesión cerrada correctamente.")
    return redirect('login')



def inicioAdmin(request):

    if not request.user.is_authenticated:
        messages.error(request, "Debes iniciar sesión como administrador.")
        return redirect('login')

    if not request.user.is_superuser:
        messages.error(request, "No tienes permiso para acceder a esta página.")
        return redirect('inicioUsuario')

    return render(request, "inicioAdmin.html")



def inicioUsuario(request):
    usuario_id = request.session.get("usuario_id")

    if not usuario_id:
        messages.warning(request, "Debes iniciar sesión primero.")
        return redirect("login")

    return render(request, "inicioUsuario.html", {
        "nombre_usuario": request.session.get("usuario_nombre")
    })




def registrar(request):
    if request.method == "POST":
        nombre = request.POST.get("nombre")
        direccion = request.POST.get("direccion")
        correo = request.POST.get("correo")
        password = request.POST.get("password")

        if Registrar.objects.filter(correo=correo).exists():
            messages.warning(request, "Este correo ya está registrado.")
            return redirect('registrar')
        Registrar.objects.create(
            nombre=nombre,
            direccion=direccion,
            correo=correo,
            contraseña=make_password(password)
        )

        messages.success(request, "Registro exitoso Ahora puedes iniciar sesión.")
        return redirect('login')

    return render(request, "Registrar.html")
