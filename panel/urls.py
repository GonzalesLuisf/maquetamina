from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('test_favicon', views.home_view, name="homeFavicon"),
    path('', views.autenticacion, name="autenticacion"),
    path('signout', views.signout, name="signout"),
    path('home', views.index, name="index"),
    path('listar', views.listar, name="listar"),
    path('agregar', views.agregar, name="agregar"),
    path('actualizar', views.actualizar, name="actualizar"),
    path('eliminar', views.eliminar, name="eliminar"),
    path('livedata', views.livedata, name="livedata"),
    path('livedata/agregar', views.livedata_agregar, name="livedata_agregar"),
    path('livedata/eliminar', views.livedata_eliminar, name="livedata_eliminar"),
    path('marcacion', views.marcacion, name="marcacion"),
    path('noregistrados', views.noregistrados, name="noregistrados"),    
]