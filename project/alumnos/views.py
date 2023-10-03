from django.shortcuts import  render
from . import forms, models


def index(request):
    return render(request, "alumnos/index.html")



def cargaAlumno(request):
    if request.method == "POST":
        form_alumno = forms.alumnoForm(request.POST)
        print(form_alumno)
        if form_alumno.is_valid():
            info = form_alumno.cleaned_data
            alumn = models.alumno(info("nombre"), info("escuela"))
            alumn.save()
            return render(request, "alumnos/index.html")
        else: 
            form_alumno = forms.alumnoForm
            return render(request, "alumnos/cargaAlumnoForm.html", {"form_alumno":form_alumno})

