from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from Aplicaciones.Animales.models import AnimalAdoptable


@login_required(login_url='login')
def lista_animales_u(request):
    animales = AnimalAdoptable.objects.all().order_by('id')
    return render(request, 'inicioU1.html', {'animales': animales})


@login_required(login_url='login')
def detalle_animal_u(request, id):
    animal = get_object_or_404(AnimalAdoptable, id=id)
    return render(request, 'usuario/animales/detalle.html', {'animal': animal})
