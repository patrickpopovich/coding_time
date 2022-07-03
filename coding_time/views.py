from multiprocessing import AuthenticationError, context
from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import redirect, render
from django.contrib.auth.forms import *
from django.contrib.auth import authenticate, login

def login_view(request):
    
    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request,user)
                context = {'message':f'Hola {username}'}
                return render(request, 'index.html', context=context)

            else:
                context = {'error': 'Usuario o contraseña incorrectos.'}
                form = AuthenticationForm()
                return render(request, 'auth/login.html', context=context)
        else:
            errors = form.errors
            form = AuthenticationForm()
            context = {'error': errors, 'form':form}
            return render(request, 'auth/login.html', context=context)
        




        

    else:
        form = AuthenticationForm()
        context = {'form':form}
        return render(request, 'auth/login.html', context=context)

def index(request):
    print(request.user)
    print(request.user.is_authenticated)
    return render(request,'index.html')



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

    
