from django.shortcuts import render
from Aplicaciones.Animales.models import AnimalAdoptable  

def lista_animalesU(request):
    animales = AnimalAdoptable.objects.all()
    return render(request, 'usuario/inicioU1.html', {'animales': animales})
