from django.db import models

# Create your models here.
class Courses(models.Model):
    name = models.CharField(max_length=69, unique = True)
    price = models.FloatField()
    description = models.CharField(max_length=269, blank = True, null= True)
    student_qty = models.IntegerField()
    difficulty_hard = models.BooleanField(default = True)