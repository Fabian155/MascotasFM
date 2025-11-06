from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from Aplicaciones.Usuario.AdopcionU.models import SolicitudAdopcion
from Aplicaciones.Adoptantes.models import Adoptante
from Aplicaciones.Animales.models import AnimalAdoptable


@login_required(login_url='login')
def solicitarA(request, animal_id):
    usuario_id = request.session.get("usuario_id")  # ID del usuario en sesión
    animal = get_object_or_404(AnimalAdoptable, id=animal_id)
    adoptante = Adoptante.objects.filter(registro_id=usuario_id).first()

    if not adoptante:
        messages.warning(request, "Antes de solicitar una adopción, completa tu registro de adoptante.")
        return redirect('adoptanteu:inicioF')

    if request.method == 'GET':
        return render(request, 'inicioU3.html', {'animal': animal})

    observacion = request.POST.get('observacion', '').strip()

    SolicitudAdopcion.objects.create(
        adoptante=adoptante,
        animal=animal,
        observacion=observacion
    )

    messages.success(request, f"Has solicitado adoptar a {animal.nombre}. Espera la respuesta del administrador.")
    return redirect('animalesu:u_animales')





@login_required(login_url='login')
def historial(request):
    usuario = request.user
    adoptante = Adoptante.objects.filter(usuario=usuario).first()

    if not adoptante:
        messages.warning(request, "Aún no tienes registro de adoptante.")
        return redirect('adoptanteu:inicioF')

    solicitudes = SolicitudAdopcion.objects.filter(adoptante=adoptante).order_by('-fecha_solicitud')
    return render(request, 'historialU.html', {'solicitudes': solicitudes})

