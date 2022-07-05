from tkinter import CASCADE
from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, related_name='profile')
    phone = models.CharField(max_length=20)
    profile_image = models.ImageField(upload_to='profile_image')

    class Meta:
        verbose_name = "Perfil "
        verbose_name_plural = "Perfiles"