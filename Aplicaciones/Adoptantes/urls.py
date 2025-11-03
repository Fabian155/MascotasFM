from django.urls import path
from. import views

urlpatterns = [
    path('', views.inicio2, name='inicioB'),
    path('nuevoAdoptado', views.nuevoAdoptado, name='nuevoAdoptado'), 
    path('GuardarAD', views.GuardarAD), 
    path('EliminarAD/<id>', views.EliminarAdoptante),
    path('editarA/<int:id>', views.editarAdoptado, name='editarAdoptado'),
    path('GuardarEdicion2', views.GuardarEdicion2, name='GuardarEdicion2'),
]