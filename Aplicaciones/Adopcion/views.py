from django.shortcuts import render, redirect
from .models import Adopcion
from Aplicaciones.Animales.models import AnimalAdoptable
from Aplicaciones.Adoptantes.models import Adoptante
from Aplicaciones.Usuario.AdopcionU.models import SolicitudAdopcion
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Count, Sum
from django.utils import timezone
import datetime

# Create your views here.

def inicio3(request):
    listAdopcion=Adopcion.objects.all()
    return render(request, "inicio3.html", {'adopcion': listAdopcion})


def nuevaAdopcion(request):
    solicitud_id = request.GET.get('solicitud_id')
    solicitud = None
    animal = None
    adoptante = None

    if solicitud_id:
        solicitud = get_object_or_404(SolicitudAdopcion, id=solicitud_id)
        animal = solicitud.animal
        adoptante = solicitud.adoptante

    # Cargas para selects
    animales = AnimalAdoptable.objects.all()
    adoptantes = Adoptante.objects.all()

    return render(request, "nuevaAdopcion.html", {
        'animal': animales,            
        'adoptante': adoptantes,      
        'solicitud_prefill': solicitud, 
        'animal_prefill': animal,
        'adoptante_prefill': adoptante,
    })


def GuardarADO(request):
    animal_id=request.POST["animal"]
    animal = AnimalAdoptable.objects.get(id=animal_id)
    adoptante_id=request.POST["adoptante"]
    adoptante = Adoptante.objects.get(id=adoptante_id)
    fecha=request.POST["fecha"]
    pago=request.POST["pago"]

    logo=request.FILES.get("logo")
    pdf = request.FILES.get("pdf")

    nuevaAdop=Adopcion.objects.create(
        animal=animal, adoptante=adoptante, fecha=fecha, pago=pago, logo=logo, pdf=pdf
    )

    solicitud_id = request.POST.get("solicitud_id")
    if solicitud_id:
        try:
            solicitud = SolicitudAdopcion.objects.get(id=solicitud_id)
            solicitud.estado = "APROBADA"
            solicitud.save()
        except SolicitudAdopcion.DoesNotExist:
            pass

    messages.success(request, "GUARDADO CORRECTAMENTE Y SOLICITUD APROBADA.")
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

def lista_solicitudes(request):
    solicitudes = SolicitudAdopcion.objects.all().order_by('-fecha_solicitud')
    return render(request, 'inicioH.html', {'solicitudes': solicitudes})


@login_required(login_url='login')
def actualizar_estado(request, solicitud_id, nuevo_estado):
    solicitud = get_object_or_404(SolicitudAdopcion, id=solicitud_id)

    solicitud.estado = nuevo_estado.upper()  
    solicitud.save()
    if nuevo_estado.upper() == "APROBADA":
        animal = solicitud.animal
        animal.estado = "ADOPTADO"
        animal.save()

    messages.success(request, f"El estado de la solicitud de {solicitud.adoptante.nombre} fue actualizado a {nuevo_estado}.")
    return redirect('lista_solicitudes')

def aprobar(request, solicitud_id):
    """
    Lleva al formulario de nueva adopción con la solicitud indicada.
    Pasamos solicitud_id por querystring para precargar adoptante/animal.
    """
    solicitud = get_object_or_404(SolicitudAdopcion, id=solicitud_id)

    if solicitud.estado.upper() == 'APROBADA':
        messages.info(request, "Esta solicitud ya fue aprobada.")
        return redirect('lista_solicitudes')
    return redirect(f"/inicioC/nuevaAdopcion?solicitud_id={solicitud.id}")

@login_required(login_url='login')
def negociosV(request):
    # Total de adopciones realizadas
    total_adopciones = Adopcion.objects.count()

    # Total recaudado (sumando precio de animales adoptados)
    total_recaudado = Adopcion.objects.aggregate(total=Sum('pago'))['total'] or 0

    # Conteo de animales por estado
    from Aplicaciones.Animales.models import AnimalAdoptable
    estado_animales = AnimalAdoptable.objects.values('estado').annotate(total=Count('id'))

    # Adopciones por mes
    adopciones_por_mes = (
        Adopcion.objects
        .values('fecha')
        .annotate(total=Count('id'))
        .order_by('fecha')
    )

    return render(request, 'Negocios.html', {
        'total_adopciones': total_adopciones,
        'total_recaudado': total_recaudado,
        'estado_animales': estado_animales,
        'adopciones_por_mes': adopciones_por_mes,
    })




