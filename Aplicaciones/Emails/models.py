from django.db import models

# Create your models here.

class Mensaje(models.Model):
    id = models.AutoField(primary_key=True)
    destinatario = models.EmailField()
    asunto = models.TextField(max_length=250)
    fecha = models.DateField(blank=True, null=True)
    fechaAct = models.DateField(blank=True, null=True)
    mensaje = models.TextField(max_length=250)
    archivo = models.FileField(upload_to='archivos_adjuntos/', null=True, blank=True)