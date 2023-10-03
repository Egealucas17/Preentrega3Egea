from django.urls import path


from . import views

app_name = "alumnos"

urlpatterns = [
    path("", views.index, name="index"),
]


urlpatterns += [
    path("cargaAlumno/", views.cargaAlumno, name = "cargaAlumno")
]


