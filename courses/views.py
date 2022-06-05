from django.shortcuts import render
from courses.models import *


# Create your views here.
def courses(request):
    cursos = Courses.objects.all()
    context = {'cursos': cursos}
    return render(request, 'courses.html', context = context)

