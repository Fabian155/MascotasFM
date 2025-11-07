from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from Aplicaciones.Login.models import Registrar
from Aplicaciones.Adoptantes.models import Adoptante


@login_required(login_url='login')
def formulario_adoptante(request):
    if request.method == "POST":
        nombre = request.POST.get("nombre")
        cedula = request.POST.get("cedula")
        direccion = request.POST.get("direccion")
        telefono = request.POST.get("telefono")
        logo = request.FILES.get("logo")
        pdf = request.FILES.get("pdf")

        # 🔹 Obtener el usuario logueado (de la tabla Registrar)
        usuario_id = request.session.get("usuario_id")
        registro = Registrar.objects.filter(id=usuario_id).first() if usuario_id else None

        # 🔹 Verificar si ya tiene ficha de adoptante
        if registro and Adoptante.objects.filter(registro=registro).exists():
            messages.warning(request, "Ya tienes un registro de adoptante.")
            return redirect('animalesu:u_animales')

        # 🔹 Crear el adoptante y vincularlo al usuario
        Adoptante.objects.create(
            registro=registro,   # 👈 aquí está la diferencia
            nombre=nombre,
            cedula=cedula,
            direccion=direccion,
            telefono=telefono,
            logo=logo,
            pdf=pdf
        )

        messages.success(request, "Tus datos se registraron correctamente. Ya puedes adoptar mascotas.")
        return redirect('animalesu:u_animales')

    return render(request, 'inicioU2.html')
