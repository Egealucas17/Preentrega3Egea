from django.urls import path


from . import views

app_name = "materia"

urlpatterns = [
    path("", views.index, name="index"),
]


urlpatterns += [
    path("cargaMateria/", views.cargaMateria, name = "cargaMateria")
]


