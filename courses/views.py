from multiprocessing import context
from re import template
from django.http import HttpResponse
from django.shortcuts import render
from courses.models import *
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse
from django.contrib.auth.forms import *
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from coding_time.forms import User_registration
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


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

def logout_view(request):
    logout(request)
    return redirect('index')

def index(request):
    print(request.user)
    print(request.user.is_authenticated)
    return render(request,'index.html')

def register_view(request):
    if request.method == 'POST':
        form = User_registration(request.POST)
        if form.is_valid():
            print('is valid')
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username = username, password=password)
            login(request, user)
            context = {'message': f'Usuario creado correctamente {username}'}
            return render(request, 'index.html', context=context)
            
        else:
            print('it is not valid')
            errors = form.errors
            form = User_registration()
            context = {'errors':errors, 'form':form}
            return render(request, 'auth/register.html', context=context)
            
       
    else:
        form = User_registration
        context = {'form':form}
        return render(request, 'auth/register.html', context = context)


class List_courses(ListView):
    model = Courses
    template_name = 'courses.html'
    queryset: Courses.objects.all()

class Detail_courses(DetailView):
    model: Courses
    template_name = 'course_detail.html'
    queryset = Courses.objects.all()

class Create_course(LoginRequiredMixin, CreateView):
    model = Courses
    template_name = 'create_course.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse('course_detail', kwargs={'pk':self.object.pk})

class Delete_course(LoginRequiredMixin,DeleteView):
    model = Courses
    template_name = 'delete_course.html'

    def get_success_url(self):
        return reverse('courses')

class Inscripcion(LoginRequiredMixin,CreateView):
    model = Estudiante
    template_name = 'inscripcion.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse('student_detail', kwargs={'pk':self.object.pk})

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

class Delete_student(LoginRequiredMixin,DeleteView):
    model = Estudiante
    template_name = 'delete_student.html'

    def get_success_url(self):
        return reverse('estudiantes')


class Update_user(LoginRequiredMixin, UpdateView):
    model = User_registration
    template_name = 'profile.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse('index', kwargs = {'pk':self.object.pk})




def search_course_view(request):
    print(request.GET)
    courses = Courses.objects.filter(name__icontains = request.GET['search'])
    context = {'courses':courses}
    return render(request, 'search_course.html', context = context)

@login_required
def contact(request):
    return render(request, 'contact.html')


class Update_course(LoginRequiredMixin, UpdateView):
    model = Courses
    template_name = 'update_course.html'
    fields= '__all__'
    

    def get_success_url(self):
        return reverse('course_detail', kwargs={'pk':self.object.pk})

class Update_student(LoginRequiredMixin, UpdateView):
    model = Courses
    template_name = 'update_student.html'
    fields= '__all__'
    

    def get_success_url(self):
        return reverse('student_detail', kwargs={'pk':self.object.pk})








