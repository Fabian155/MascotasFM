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
        logo = request.FILES.get("logo")
        pdf = request.FILES.get("pdf")

        Adoptante.objects.create(
            nombre=nombre,
            cedula=cedula,
            direccion=direccion,
            telefono=telefono,
            logo=logo,   
            pdf=pdf      
        )

        messages.success(request, "Tus datos se registraron correctamente.")
        return redirect('adoptanteu:inicioF')

    return render(request, 'inicioU2.html')
