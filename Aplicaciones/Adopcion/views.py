from django.shortcuts import render, redirect
from .models import Adopcion
from Aplicaciones.Animales.models import AnimalAdoptable
from Aplicaciones.Adoptantes.models import Adoptante
from django.contrib import messages
from django.shortcuts import get_object_or_404

# Create your views here.

def inicio3(request):
    listAdopcion=Adopcion.objects.all()
    return render(request, "inicio3.html", {'adopcion': listAdopcion})


def nuevaAdopcion(request):
    animal=AnimalAdoptable.objects.all()
    adoptante=Adoptante.objects.all()
    return render(request, "nuevaAdopcion.html", {'animal': animal, 'adoptante': adoptante})

def GuardarADO(request):
    animal_id=request.POST["animal"]
    animal = AnimalAdoptable.objects.get(id=animal_id)
    adoptante_id=request.POST["adoptante"]
    adoptante = Adoptante.objects.get(id=adoptante_id)
    fecha=request.POST["fecha"]
    pago=request.POST["pago"]

    logo=request.FILES.get("logo")
    pdf = request.FILES.get("pdf")

    nuevaAdop=Adopcion.objects.create(animal=animal, adoptante=adoptante, fecha=fecha, pago=pago, logo=logo, pdf=pdf)
    messages.success(request, "GUARDADO CORRECTAMENTE")
    return redirect('inicioC')

def EliminarAdopcion(request, id):
    EliminarADOP=Adopcion.objects.get(id=id)
    EliminarADOP.delete()
    return redirect('inicioC')


def editarAdopcion(request, id):
    editaAdop=get_object_or_404(Adopcion, id=id)
    animalS=AnimalAdoptable.objects.all()
    adoptantE=Adoptante.objects.all()
    return render(request, "editarAdopcion.html", {'editarADO': editaAdop, 'animal': animalS, 'adoptante': adoptantE })

def GuardarEdicion3(request):
    id=request.POST["id"]
    animal_id=request.POST["animal"]
    adoptante_id=request.POST["adoptante"]
    fecha=request.POST["fecha"]
    pago=request.POST["pago"].replace(',','.')

    editale=Adopcion.objects.get(id=id)
    nuevo_logo = request.FILES.get("logo")
    nuevo_pdf = request.FILES.get("pdf")

    editale.animal = AnimalAdoptable.objects.get(id=animal_id)
    editale.adoptante = Adoptante.objects.get(id=adoptante_id)
    editale.fecha=fecha
    editale.pago=pago
    if nuevo_logo:
        editale.logo = nuevo_logo
    if nuevo_pdf:
        editale.pdf = nuevo_pdf
    editale.save()
    messages.success(request, "Actualizacion correcta")
    return redirect('inicioC')



