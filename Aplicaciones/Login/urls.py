from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicioSesion, name='login'),
    path('cerrarSesion/', views.cerrarSesion, name='cerrarSesion'),
    path('inicioAdmin/', views.inicioAdmin, name='inicioAdmin'),
    path('inicioUsuario/', views.inicioUsuario, name='inicioUsuario'),
]
