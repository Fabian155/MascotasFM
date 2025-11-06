from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from Aplicaciones.Animales.models import AnimalAdoptable
from Aplicaciones.Adoptantes.models import Adoptante
from Aplicaciones.Login.models import Registrar

@login_required(login_url='login')
def lista_animales_u(request):
    animales = AnimalAdoptable.objects.filter(estado="DISPONIBLE")

    registro_id = request.session.get("usuario_id")
    registro = None
    if registro_id:
        registro = Registrar.objects.filter(id=registro_id).first()

    tiene_perfil_adoptante = False
    if registro:
        tiene_perfil_adoptante = Adoptante.objects.filter(registro=registro).exists()

    return render(
        request,
        'inicioU1.html',
        {'animales': animales, 'tiene_perfil_adoptante': tiene_perfil_adoptante}
    )


@login_required(login_url='login')
def detalle_animal_u(request, id):
    animal = get_object_or_404(AnimalAdoptable, id=id)
    return render(request, 'usuario/animales/detalle.html', {'animal': animal})
