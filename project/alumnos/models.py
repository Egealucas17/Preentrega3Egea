from django.db import models



class alumno(models.Model):

    nombre = models.CharField(max_length=40)
    escuela = models.CharField(max_length=20)
    año = models.IntegerField(null= "True" , blank= "true", default= "1")
    nivel = models.CharField(max_length=10, null= "True" , blank= "true")

    
    def __str__(self):
        return f"{self.nombre}"
