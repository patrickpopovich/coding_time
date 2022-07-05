
from django.shortcuts import render
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from users.models import Profile
from django.views.generic import ListView
# Create your views here.

class List_profiles(ListView):
    model = Profile
    template_name = 'profiles.html'
    queryset: Profile.objects.all()
    print(Profile.objects.all())