from django import forms
from . import models



class profesorForm(forms.ModelForm):
    class Meta:
        model = models.profesor
        fields = ["nombre" , "nivel", "materia_id"]

   