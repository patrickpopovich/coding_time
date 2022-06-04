from django.http import HttpResponse
from datetime import datetime
def saludo(request, nombre):
    return HttpResponse(f"hola bebe {nombre}")

def despedida(request):
    return HttpResponse('Grazie mille')

def fecha_actual(request):
    fecha = datetime.now().date()
    mensaje = f'hoy es {fecha}'
    return HttpResponse(mensaje)

