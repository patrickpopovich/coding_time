from django.http import HttpResponse
from django.shortcuts import render
from courses.models import *
from courses.forms import Student_Form


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

def inscripcion(request):
    if request.method == 'GET':

        form = Student_Form()
        context = {'form':form}
        return render(request, 'inscripcion.html', context=context )

    else:
        form = Student_Form(request.POST)
        if form.is_valid():
            new_student = Estudiante.objects.create(
                name = form.cleaned_data['name'],
                last_name = form.cleaned_data['last_name'],
                identification = form.cleaned_data['identification']

            )
            context = {'new_student':new_student}
        return render(request, 'inscripcion.html', context=context )








