from django.shortcuts import render, redirect
from .models import Mensaje
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from django.core.mail import EmailMessage
import mimetypes
import os
from datetime import date

# Create your views here.

def inicio4(request):
    listaEmails=Mensaje.objects.all()
    return render(request, "inicio4.html", {'Emails': listaEmails})


def nuevoCorreo(request):
    return render(request, "nuevoCorreo.html", { "hoy": date.today().isoformat() })

def GuardarCO(request):
    destinatario=request.POST["destinatario"]
    asunto=request.POST["asunto"]
    fecha=request.POST["fecha"]
    fechaAct=request.POST["fechaAct"]
    mensaje=request.POST["mensaje"]
    archivo = request.FILES.get("archivo")
    nuevoMensaje=Mensaje.objects.create(destinatario=destinatario, asunto=asunto, fecha=fecha, fechaAct=fechaAct, mensaje=mensaje, archivo=archivo)
    email_a_enviar = EmailMessage(
        subject=asunto,
        body=mensaje,
        from_email=settings.EMAIL_HOST_USER,
        to=[destinatario],
    )
    if archivo:
        try:
            # Es crucial reposicionar el puntero del archivo si ya fue leído (ej. por models.create)
            archivo.seek(0)
            email_a_enviar.attach(archivo.name, archivo.read(), archivo.content_type)
        except Exception as e:
            messages.error(request, f"Error al adjuntar el archivo: {e}. El correo se enviará sin el adjunto.")
    try:
        email_a_enviar.send(fail_silently=False)
        messages.success(request, "Mensaje creado y enviado exitosamente.")
    except Exception as e:
        messages.error(request, f"Error al enviar el mensaje: {e}. Por favor, revisa la configuración del correo.")
        # Opcional: print(f"Error en el envío de correo: {e}") para depurar en la consola
    #antes del redirec poner lso siguiente/mensaje de confirmacion/creas mos un mensaje d eocnfirmaicon con success
    messages.success(request,"Mensjae creado exitosamnete")
    return redirect('inicioD')

def editarCorreo(request, id):
    mensajeEditar = Mensaje.objects.get(id=id)
    return render(request, "editarCorreo.html", {'EditarM': mensajeEditar, "hoy": date.today().isoformat() })

def EliminarCorreo(request, id):
    EliminarCO=Mensaje.objects.get(id=id)
    #Eliminar archivo adjunto si existe
    if EliminarCO.archivo and os.path.isfile(EliminarCO.archivo.path):
        os.remove(EliminarCO.archivo.path)
        EliminarCO.delete()
        messages.success(request, "Mensaje ELIMINADO exitosamente")
        return redirect('inicioD')


def GuardarEdicion4(request):
    id = request.POST["id"]
    destinatario = request.POST["destinatario"]
    asunto = request.POST["asunto"]
    fecha = request.POST["fecha"]
    fechaAct = request.POST["fechaAct"]
    mensajetxt = request.POST["mensaje"]
    archivo = request.FILES.get("archivo")

    mensaje = Mensaje.objects.get(id=id)
    mensaje.destinatario = destinatario
    mensaje.asunto = asunto
    mensaje.mensaje = mensajetxt
    mensaje.fecha = fecha
    mensaje.fechaAct = fechaAct

    # Si hay un nuevo archivo, reemplazar el anterior
    if archivo:
        if mensaje.archivo and os.path.isfile(mensaje.archivo.path):
            os.remove(mensaje.archivo.path)
        mensaje.archivo = archivo

    # Guardar SIEMPRE
    mensaje.save()
    messages.success(request, "Mensaje ACTUALIZADO exitosamente")
    return redirect('inicioD')  # <-- Asegúrate de que 'inicioD' exista en tus urls


# Enviar mensaje por correo
def enviarMensaje(request, id):
    mensaje = get_object_or_404(Mensaje, id=id)

    # Limpiar el destinatario
    destinatario = mensaje.destinatario.strip()

    email = EmailMessage(
        subject=mensaje.asunto,
        body=mensaje.mensaje,
        from_email=settings.EMAIL_HOST_USER,
        to=[destinatario],
    )

    # Adjuntar si hay archivo
    if mensaje.archivo:
        file_type, _ = mimetypes.guess_type(mensaje.archivo.name)
        with open(mensaje.archivo.path, 'rb') as f:
            email.attach(mensaje.archivo.name, f.read(), file_type)

    # Enviar con manejo de error
    try:
        email.send(fail_silently=False)
        messages.success(request, "Mensaje ENVIADO exitosamente")
    except Exception as e:
        messages.error(request, f"ERROR al enviar el correo: {e}")

    return redirect('inicioD')


