from django.contrib import admin
from courses.models import *
# Register your models here.
@admin.register(Courses) 
class CoursesAdmin(admin.ModelAdmin):
    list_display = ['name','price','description','student_qty','difficulty_hard']

@admin.register(Estudiante)
class EstudianteAdmin(admin.ModelAdmin):
    list_display = ['name','last_name','identification']


@admin.register(Trabajo) 
class TrabajoAdmin(admin.ModelAdmin):
    list_display = ['name']
