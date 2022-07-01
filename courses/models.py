from tabnanny import verbose
from django.db import models

# Create your models here.
class Courses(models.Model):
    name = models.CharField(max_length=69, unique = True)
    price = models.FloatField()
    description = models.CharField(max_length=269, blank = True, null= True)
    student_qty = models.IntegerField()
    difficulty_hard = models.BooleanField(default = True)

    class Meta:
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"

class Estudiante(models.Model):
    name = models.CharField(max_length=69)
    last_name = models.CharField(max_length=69)
    identification = models.IntegerField(unique=True)

    class Meta:
        verbose_name = "Estudiante"
        verbose_name_plural = "Estudiantes"

class Trabajo(models.Model):
    name = models.CharField(max_length=69)
    delivered = models.BooleanField(default = False)

    class Meta:
        verbose_name = "Trabajo"
        verbose_name_plural = "Trabajos"

    