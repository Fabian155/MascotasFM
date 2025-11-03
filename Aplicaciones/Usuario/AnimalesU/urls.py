from django.urls import path
from . import views

app_name = 'animalesu'

urlpatterns = [
    path('', views.lista_animales_u, name='u_animales'),
    path('<int:id>/', views.detalle_animal_u, name='inicioE'),
]
