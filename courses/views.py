from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render
from courses.models import *
from courses.forms import Student_Form


# Create your views here.
def courses(request):
    cursos = Courses.objects.all()
    context = {'cursos': cursos}
    return render(request, 'courses.html', context = context)

def course_detail(request, pk):
    try:
        course = Courses.objects.get(id=pk)
        context = {'course':course}
        return render(request, 'course_detail.html', context=context)
    except:
        context = {'error': 'No se pudo encontrar el curso.'}
        return render(request,'courses.html', context = context)


def show_students(request):
    students = Estudiante.objects.all()
    context = {'students': students}
    return render(request, 'estudiantes.html', context = context)

def student_detail(request, pk):
    try:
        student = Estudiante.objects.get(id=pk)
        context = {'student':student}
        return render(request, 'student_detail.html', context=context)
    except:
        context = {'error': 'No se pudo encontrar el estudiante.'}
        return render(request,'estudiantes.html', context = context)

def delete_student(request, pk):
    try:
        if request.method == 'GET':
            student = Estudiante.objects.get(id=pk)
            context = {'student':student}
    
        else:
            student = Estudiante.objects.get(id=pk)
            student.delete()
            context = {'message':'Futuro autodidacta eliminado con éxito.'}
        return render(request, 'delete_student.html', context=context)
    except:
            context = {'error': 'No se pudo encontrar el estudiante.'}
            return render(request,'delete_student.html', context = context)



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

def entregar_trabajo(request):
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

def search_course_view(request):
    print(request.GET)
    courses = Courses.objects.filter(name__icontains = request.GET['search'])
    context = {'courses':courses}
    return render(request, 'search_course.html', context = context)









