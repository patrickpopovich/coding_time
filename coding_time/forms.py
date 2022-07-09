from dataclasses import field
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class User_registration(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Tu contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Tu contraseña de nuevo', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        help_texts = {p:'' for p in fields}

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Tu contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Tu contraseña de nuevo', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email', 'password', 'password']


