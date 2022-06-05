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

urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludo/<nombre>/', saludo, name = 'saludo'),
    path('', index, name = 'index'),
    path('fecha_de_hoy', fecha_actual, name = 'fecha actual'),
    path('probando_template/', probando_template, name = 'probando_template'),
    path('courses/', include('courses.urls')),
    path('estudiantes/', show_students, name = 'estudiantes'),
    path('trabajos/', trabajos, name = 'trabajos') 
]   
