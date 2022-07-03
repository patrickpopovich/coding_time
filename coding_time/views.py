from multiprocessing import AuthenticationError, context
from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import redirect, render
from django.contrib.auth.forms import *
from django.contrib.auth import authenticate, login, logout




def saludo(request, nombre):
    return HttpResponse(f"hola bebe que talco {nombre}")



def fecha_actual(request):
    fecha = datetime.now().date()
    mensaje = f'hoy es {fecha}'
    return HttpResponse(mensaje)

def probando_template(request):
    context = {
        'nombre':'Patrick',
        'apellido':'Popovich',

        'lenguajes':['Python','Scala','Ruby','Java','Javascript','Cobol','Perl']

        
    }
    return render(request, 'template_1.html', context =context)

def search_course_view(request):
    print(request.GET)
    courses = Courses.objects.filter(name__icontains = request.GET['search'])
    context = {'courses':courses}
    return render(request, 'search_course.html', context = context)

    
