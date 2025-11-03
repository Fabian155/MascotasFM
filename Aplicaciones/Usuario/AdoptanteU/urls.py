from django.urls import path
from . import views

app_name = 'adoptanteu'

urlpatterns = [
    path('', views.formulario_adoptante, name='inicioF'),
]
