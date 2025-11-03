from django.urls import path
from . import views

app_name = 'adopcionu'

urlpatterns = [
    path('solicitar/<int:animal_id>/', views.solicitarA, name='inicioG'),
    path('historial/', views.historial, name='u_historial'),
]
