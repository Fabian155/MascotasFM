from django.db import models
from Aplicaciones.Adoptantes.models import Adoptante
from Aplicaciones.Animales.models import AnimalAdoptable

# Create your models here.

class SolicitudAdopcion(models.Model):
    id = models.AutoField(primary_key=True)
    adoptante = models.ForeignKey(Adoptante, on_delete=models.CASCADE)
    animal = models.ForeignKey(AnimalAdoptable, on_delete=models.CASCADE)
    fecha_solicitud = models.DateField(auto_now_add=True)
    estado = models.CharField(
        max_length=20,
        choices=[
            ('PENDIENTE', 'Pendiente'),
            ('APROBADA', 'Aprobada'),
            ('RECHAZADA', 'Rechazada'),
        ],
        default='PENDIENTE'
    )

    observacion = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.adoptante.nombre} solicitó adoptar a {self.animal.nombre}"
