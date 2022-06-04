from django.http import HttpResponse

def saludo(request):
    return HttpResponse("¡Hola! Bienvenido a Coding Time")


def ver_cursos(request):
    return HttpResponse("Acá se ven los cursos disponibles")

def agregar_cursos(request):
    return HttpResponse("Acá se pueden agregar mas cursos")