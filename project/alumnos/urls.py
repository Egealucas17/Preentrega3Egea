from django.urls import path
from django.views.generic import TemplateView

from . import views

app_name = "alumnos"

urlpatterns = [
    path("", views.index, name="index"),
]


urlpatterns += [
    path("carga/", views.carga, name = "carga")
]


