from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    path('listado_articulos/', views.list_art, name='listado_articulos'),
    path('listado_categorias/', views.list_cat, name='listado_categorias'),
]