from django.shortcuts import  render, redirect
from . import forms, models


def index(request):
    return render(request, "alumnos/index.html")



def cargaAlumno(request):

        if request.method == "POST":
            form = forms.alumnoForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect("alumnos:index")
            
        else: 
            form = forms.alumnoForm()
        return render(request, "alumnos/cargaAlumnoForm.html", {"form": form})

