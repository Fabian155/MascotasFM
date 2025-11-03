from django.urls import path
from. import views

urlpatterns = [
    path('', views.inicio3, name='inicioC'),
    path('nuevaAdopcion', views.nuevaAdopcion, name='nuevaAdopcion'), 
    path('GuardarADO', views.GuardarADO), 
    path('EliminarADOP/<id>', views.EliminarAdopcion),
    path('editarADO/<int:id>', views.editarAdopcion, name='editarAdopcion'),
    path('GuardarEdicion3', views.GuardarEdicion3, name='GuardarEdicion3'),
    path('solicitudes/', views.lista_solicitudes, name='lista_solicitudes'),
    path('solicitudes/estado/<int:solicitud_id>/<str:nuevo_estado>/', views.actualizar_estado, name='actualizar_estado'),
]