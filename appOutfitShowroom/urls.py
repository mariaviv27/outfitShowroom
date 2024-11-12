from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('outfits/', views.lista_outfits, name='lista_outfits'),
    path('outfits/<int:outfit_id>/', views.detalle_outfit, name='detalle_outfit'),
    path('ocasiones/', views.lista_ocasiones, name='lista_ocasiones'),
    path('ocasiones/<int:ocasion_id>/', views.detalle_ocasion, name='detalle_ocasion'),
    path('estilos/', views.lista_estilos, name='lista_estilos'),
    path('estilos/<int:estilo_id>/', views.detalle_estilo, name='detalle_estilo'),
]
