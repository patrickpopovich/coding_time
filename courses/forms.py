from django import forms

from courses.models import Trabajo

class Student_Form(forms.Form):
    name = forms.CharField(max_length=69)
    last_name = forms.CharField(max_length=69)
    identification = forms.IntegerField()

