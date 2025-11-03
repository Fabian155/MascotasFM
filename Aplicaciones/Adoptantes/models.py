from django.db import models

# Create your models here.



class Adoptante(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.TextField()
    cedula = models.TextField()
    direccion = models.TextField()
    telefono = models.TextField()

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
        return f"{self.nombre} - {self.cedula}"