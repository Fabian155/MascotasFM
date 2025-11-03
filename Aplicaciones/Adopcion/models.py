from django.db import models
from Aplicaciones.Adoptantes.models import Adoptante
from Aplicaciones.Animales.models import AnimalAdoptable

# Create your models here.

class Adopcion(models.Model):
    id = models.AutoField(primary_key=True)
    animal = models.ForeignKey(AnimalAdoptable, on_delete=models.CASCADE)
    adoptante = models.ForeignKey(Adoptante, on_delete=models.CASCADE)
    fecha = models.DateField(blank=True, null=True)
    pago = models.TextField()
    
    logo = models.FileField(
        upload_to='cargos',  
        null=True,            
        blank=True            
    )

    pdf = models.FileField(
        upload_to='pdfs',  
        blank=True
    )
    
    def __str__(self):
        return f"Adopción de {self.animal.nombre} por {self.adoptante.nombre} el {self.fecha}"


