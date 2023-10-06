from django.db import models



class profesor(models.Model):

    nombre = models.CharField(max_length=40)
    nivel = models.CharField(max_length=10, null= "True" , blank= "true")
    materia = models.CharField(max_length=40)

    
    def __str__(self):
        return f"{self.nombre}"
