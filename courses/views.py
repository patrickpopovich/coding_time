from django.shortcuts import render
from courses.models import *


# Create your views here.
def courses(request):
    cursos = Courses.objects.all()
    context = {'cursos': cursos}
    return render(request, 'courses.html', context = context)

def show_students(request):
    students = Estudiante.objects.all()
    context = {'students': students}
    return render(request, 'estudiantes.html', context = context)

def trabajos(request):
    entregas = Trabajo.objects.all()
    context = {'entregas' : entregas}
    return render(request,'trabajos.html', context=context)


