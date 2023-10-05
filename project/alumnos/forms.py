from django import forms
from . import models



class alumnoForm(forms.ModelForm):
    class Meta:
        model = models.alumno
        fields = ["nombre" , "escuela"]

   