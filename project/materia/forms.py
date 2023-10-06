from django import forms
from . import models



class materiaForm(forms.ModelForm):
    class Meta:
        model = models.materia
        fields = ["nombre" , "nivel"]

   