from django.shortcuts import  render, redirect
from django.http import HttpResponse
from . import forms, models


def index(request):
    return render(request, "profesor/index.html")



def cargaProfesor(request):

        if request.method == "POST":
            form = forms.profesorForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect("profesor:index")
            
        else: 
            form = forms.profesorForm()
        return render(request, "profesor/cargaProfesorForm.html", {"form": form})



