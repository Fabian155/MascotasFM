from django.shortcuts import render, redirect
from .models import AnimalAdoptable
from django.shortcuts import get_object_or_404
from django.contrib import messages

# Create your views here.

def inicio1(request):
    listaAnimal=AnimalAdoptable.objects.all()
    return render(request, "inicio1.html", {'Animals': listaAnimal})


def nuevaMascota(request):
    return render(request, "nuevaMascota.html")

def GuardarA(request):
    nombre=request.POST["nombre"]
    especieid=request.POST["especieid"]
    edad=request.POST["edad"]
    salud=request.POST["salud"]

    logo=request.FILES.get("logo")
    pdf = request.FILES.get("pdf")

    nuevoAnimal=AnimalAdoptable.objects.create(nombre=nombre, especieid=especieid, edad=edad, salud=salud, logo=logo, pdf=pdf)
    messages.success(request, "GUARDADO CORRECTA MENTE")
    return redirect('/')

def EliminarAnimal(request, id):
    EliminarA=AnimalAdoptable.objects.get(id=id)
    EliminarA.delete()
    return redirect('/')


def editarMascota(request, id):
    editarMas=get_object_or_404(AnimalAdoptable, id=id)
    return render(request, "editarMascota.html", {'editarM': editarMas })

def GuardarEdicion1(request):
    id=request.POST["id"]
    nombre=request.POST["nombre"]
    especieid=request.POST["especieid"]
    edad=request.POST["edad"]
    salud=request.POST["salud"].replace(',','.')

    editele=AnimalAdoptable.objects.get(id=id)
    nuevo_logo = request.FILES.get("logo")
    nuevo_pdf = request.FILES.get("pdf")

    editele.nombre=nombre
    editele.especieid=especieid
    editele.edad=edad
    editele.salud=salud
    
    if nuevo_logo:
        editele.logo = nuevo_logo
    if nuevo_pdf:
        editele.pdf = nuevo_pdf
    editele.save()
    messages.success(request, "Actualizacion correcta")
    return redirect('/')

