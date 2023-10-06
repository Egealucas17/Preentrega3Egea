from django.db import models

from django.db import models



class materia(models.Model):

    nombre = models.CharField(max_length=40)
    nivel = models.CharField(max_length=10, null= "True" , blank= "true")

    
    def __str__(self):
        return f"{self.nombre}"
