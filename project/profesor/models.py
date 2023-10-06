from django.db import models
from materia import models as m



class profesor(models.Model):

    nombre = models.CharField(max_length=40)
    nivel = models.CharField(max_length=10, null= "True" , blank= "true")
    materia_id = models.ForeignKey(m.materia, on_delete = models.SET_NULL , null= "True", blank= "True")

    
    def __str__(self):
        return f"{self.nombre}"
