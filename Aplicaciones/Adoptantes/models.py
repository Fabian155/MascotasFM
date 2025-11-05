from django.db import models

# Create your models here.



class Adoptante(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.TextField()
    cedula = models.TextField()
    direccion = models.TextField()
    telefono = models.TextField()
    correo = models.EmailField(max_length=254, null=True, blank=True)   
    password = models.CharField(max_length=128, null=True, blank=True)

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