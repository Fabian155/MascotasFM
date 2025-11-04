from django.db import models

# Create your models here.

class AnimalAdoptable(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.TextField()
    especieid = models.TextField()
    edad = models.TextField()
    salud = models.TextField()
    
    logo = models.FileField(
        upload_to='cargos',
        null=True,
        blank=True
    )

    pdf = models.FileField(
        upload_to='pdfs',
        blank=True
    )

    precio = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    estado = models.CharField(
        max_length=15,
        choices=[('DISPONIBLE', 'DISPONIBLE'), ('ADOPTADO', 'ADOPTADO')],
        default='DISPONIBLE'
    )

    def __str__(self):
        return self.nombre
