from django import forms
from . import models



class alumnoForm(forms.ModelForm):
    class Meta:
        model = models.materia
        fields = ["nombre" , "nivel"]

   