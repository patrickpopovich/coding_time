"""coding_time URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from itertools import product
from django.contrib import admin
from django.urls import path, include

from courses.views import *
from coding_time.views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', index, name = 'index'),
    path('courses/', include('courses.urls')),
    path('estudiantes/', show_students, name = 'estudiantes'),
    path('inscripcion/', Inscripcion.as_view(), name = 'inscripcion'),
    path('student_detail/<int:pk>/', student_detail, name = 'student_detail'),
    path('delete_student/<int:pk>/', Delete_student.as_view(), name = 'delete_student'),
    path('delete_course/<int:pk>/', Delete_course.as_view(), name = 'delete_course'),
    path('', List_courses.as_view(), name = 'list_courses'), 
    path('create_course/', Create_course.as_view(), name = 'create_course'),
    path('login/', login_view, name = 'login'),
    path('logout/', logout_view, name = 'logout'),
    path('register/', register_view, name = 'register'),
    path('contact/', contact, name = 'contact'),
    path('profile/', Update_user.as_view(), name = 'profile'),
    path('update_course/<int:pk>/', Update_course.as_view(), name = 'update_course'),
    path('update_student/<int:pk>/', Update_student.as_view(), name = 'update_student'),

   
]   + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)