from django.urls import path


from . import views

app_name = "profesor"

urlpatterns = [
    path("", views.index, name="index"),
]


urlpatterns += [
    path("cargaProfesor/", views.cargaProfesor, name = "cargaProfesor")
]


