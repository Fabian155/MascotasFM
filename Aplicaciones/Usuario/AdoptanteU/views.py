from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from Aplicaciones.Adoptantes.models import Adoptante  # Importamos el modelo del admin


@login_required(login_url='login')
def formulario_adoptante(request):
    if request.method == "POST":
        nombre = request.POST.get("nombre")
        cedula = request.POST.get("cedula")
        direccion = request.POST.get("direccion")
        telefono = request.POST.get("telefono")

        # Guardar datos en la tabla original de Adoptantes (admin)
        Adoptante.objects.create(
            nombre=nombre,
            cedula=cedula,
            direccion=direccion,
            telefono=telefono
        )
        messages.success(request, "Tus datos se registraron correctamente.")
        return redirect('adoptanteu:u_form_adoptante')

    return render(request, 'formularioU.html')
