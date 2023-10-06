from django import forms
from . import models



class alumnoForm(forms.ModelForm):
    class Meta:
        model = models.profesor
        fields = ["nombre" , "nivel", "materia"]

   