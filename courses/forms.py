from django import forms
from django.db import models


class Student_Form(forms.Form):
    name = forms.CharField(max_length=69)
    last_name = forms.CharField(max_length=69)
    identification = forms.IntegerField()
    image = models.ImageField(upload_to = 'users', blank=True, null=True)

