from django.shortcuts import render, redirect
from .models import Adoptante
from django.shortcuts import get_object_or_404
from django.contrib import messages

# Create your views here.

def inicio2(request):
    listaAdop=Adoptante.objects.all()
    return render(request, "inicio2.html", {'Adoptador': listaAdop})


def nuevoAdoptado(request):
    return render(request, "nuevoAdoptado.html")

def GuardarAD(request):
    nombre=request.POST["nombre"]
    cedula=request.POST["cedula"]
    direccion=request.POST["direccion"]
    telefono=request.POST["telefono"]

    logo=request.FILES.get("logo")
    pdf = request.FILES.get("pdf")

    nuevoAdoptan=Adoptante.objects.create(nombre=nombre, cedula=cedula, direccion=direccion, telefono=telefono, logo=logo, pdf=pdf)
    messages.success(request, "GUARDADO CORRECTAMENTE")
    return redirect('inicioB')

def EliminarAdoptante(request, id):
    EliminarAD=Adoptante.objects.get(id=id)
    EliminarAD.delete()
    return redirect('inicioB')


def editarAdoptado(request, id):
    editarADOP=get_object_or_404(Adoptante, id=id)
    return render(request, "editarAdoptado.html", {'editarA': editarADOP })

def GuardarEdicion2(request):
    id=request.POST["id"]
    nombre=request.POST["nombre"]
    cedula=request.POST["cedula"]
    direccion=request.POST["direccion"]
    telefono=request.POST["telefono"].replace(',','.')

    edital=Adoptante.objects.get(id=id)
    nuevo_logo = request.FILES.get("logo")
    nuevo_pdf = request.FILES.get("pdf")

    edital.nombre=nombre
    edital.cedula=cedula
    edital.direccion=direccion
    edital.telefono=telefono
    
    if nuevo_logo:
        edital.logo = nuevo_logo
    if nuevo_pdf:
        edital.pdf = nuevo_pdf
    edital.save()
    messages.success(request, "Actualizacion correcta")
    return redirect('inicioB')

