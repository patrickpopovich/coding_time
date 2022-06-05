from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render

def saludo(request, nombre):
    return HttpResponse(f"hola bebe que talco {nombre}")

def despedida(request):
    return HttpResponse('Grazie mille')

def fecha_actual(request):
    fecha = datetime.now().date()
    mensaje = f'hoy es {fecha}'
    return HttpResponse(mensaje)

def probando_template(request):
    return render(request, 'template_1.html', context ={})

    
