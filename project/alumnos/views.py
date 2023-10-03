from django.shortcuts import redirect, render
from . import forms, models


def index(request):
    alumno = models.alumno.objects.all()
    #contexto = {"Alumnos":alumno}
    return render(request, "alumnos/index.html")



def carga(request):
    if request.method == "POST":
        form = forms.alumnoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("alumnos:index")
        else: 
            form = forms.alumnoForm
            return render(request, "alumnos/carga.html", {"form:form"})

