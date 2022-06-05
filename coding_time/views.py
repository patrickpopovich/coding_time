from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render

def saludo(request, nombre):
    return HttpResponse(f"hola bebe que talco {nombre}")


def index(request):
    return render(request,'index.html')

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

    
