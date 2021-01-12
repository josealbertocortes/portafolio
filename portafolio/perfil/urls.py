from django.urls import path

from . import views

urlpatterns = [
	#Leave as empty string for base url
	path('', views.perfil, name="perfil"),
    path('trabajos', views.trabajos, name="trabajos"),
    path('estudios', views.estudios, name="estudios"),


]