from django.urls import path
from .import views

urlpatterns = [
    path('inicio4/', views.inicio4, name='inicioD'),
    path('nuevoCorreo/', views.nuevoCorreo, name='nuevoCorreo'),
    path('GuardarCO/', views.GuardarCO, name='GuardarCO'),
    path('EliminarCO/<int:id>/', views.EliminarCorreo, name='EliminarCO'),
    path('EditarM/<int:id>/', views.editarCorreo, name='editarM'),
    path('GuardarEdicion4/', views.GuardarEdicion4, name='GuardarEdicion4'),
    path('enviarMensaje/<int:id>/', views.enviarMensaje),
]
