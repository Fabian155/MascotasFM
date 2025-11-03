from django.urls import path
from. import views

urlpatterns = [
    path('', views.inicio1, name='inicioA'),
    path('nuevaMascota', views.nuevaMascota, name='nuevaMascota'), 
    path('GuardarA', views.GuardarA), 
    path('EliminarA/<id>', views.EliminarAnimal),
    path('editarM/<int:id>', views.editarMascota, name='editarMascota'),
    path('GuardarEdicion1', views.GuardarEdicion1, name='GuardarEdicion1'),
]