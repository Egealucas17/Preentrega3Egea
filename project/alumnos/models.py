from django.db import models



class alumno(models.Model):

    nombre = models.CharField(max_length=40)
    escuela = models.CharField(max_length=20)

    
    def __str__(self):
        return f"{self.nombre}"
