from django.shortcuts import  render, redirect
from . import forms, models


def index(request):
    return render(request, "materia/index.html")



def cargaMateria(request):

        if request.method == "POST":
            form = forms.materiaForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect("materia:index")
            
        else: 
            form = forms.materiaForm()
        return render(request, "materia/cargaMateriaForm.html", {"form": form})
