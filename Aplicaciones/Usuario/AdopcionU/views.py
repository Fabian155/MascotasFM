from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from Aplicaciones.Usuario.AdopcionU.models import SolicitudAdopcion
from Aplicaciones.Adoptantes.models import Adoptante
from Aplicaciones.Animales.models import AnimalAdoptable


@login_required(login_url='login')
def solicitarA(request, animal_id):
    animal = get_object_or_404(AnimalAdoptable, id=animal_id)
    adoptante = Adoptante.objects.filter(nombre=request.user.first_name).first()

    if request.method == 'POST':
        observacion = request.POST.get('observacion')

        if not adoptante:
            messages.warning(request, "Debes registrar tus datos en el módulo de Adoptante antes de solicitar una adopción.")
            return redirect('adoptanteu:inicioF')
        SolicitudAdopcion.objects.create(
            adoptante=adoptante,
            animal=animal,
            observacion=observacion
        )
        messages.success(request, f"Has solicitado adoptar a {animal.nombre}. Espera la respuesta del administrador.")
        return redirect('animalesu:u_animales')

    return render(request, 'inicioU3.html', {'animal': animal})


@login_required(login_url='login')
def historial(request):
    # Mostrar solo las solicitudes hechas por el usuario actual
    solicitudes = SolicitudAdopcion.objects.filter(adoptante__nombre=request.user.first_name)
    return render(request, 'historialU.html', {'solicitudes': solicitudes})
