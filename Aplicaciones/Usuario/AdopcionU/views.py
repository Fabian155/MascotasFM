from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from Aplicaciones.Usuario.AdopcionU.models import SolicitudAdopcion
from Aplicaciones.Adoptantes.models import Adoptante
from Aplicaciones.Animales.models import AnimalAdoptable


@login_required(login_url='login')
def solicitarA(request, animal_id):
    animal = get_object_or_404(AnimalAdoptable, id=animal_id)

    if request.method == 'GET':
        return render(request, 'inicioU3.html', {'animal': animal})
    observacion = request.POST.get('observacion', '').strip()

    if not Adoptante.objects.exists():
        messages.warning(request, "Debes registrar tus datos antes de solicitar una adopción.")
        return redirect('adoptanteu:inicioF')
    adoptante = Adoptante.objects.latest('id')

    SolicitudAdopcion.objects.create(
        adoptante=adoptante,
        animal=animal,
        observacion=observacion
    )

    messages.success(request, f"Has solicitado adoptar a {animal.nombre}. Espera la respuesta del administrador.")
    return redirect('animalesu:u_animales')



@login_required(login_url='login')
def historial(request):
    """
    Muestra todas las solicitudes del usuario actual.
    Si más adelante enlazas usuarios con adoptantes,
    aquí se puede filtrar por el adoptante que pertenece al usuario logueado.
    """
    solicitudes = SolicitudAdopcion.objects.all().order_by('-fecha_solicitud')
    return render(request, 'historialU.html', {'solicitudes': solicitudes})
