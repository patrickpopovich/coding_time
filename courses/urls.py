
from django.urls import path

from courses.views import *


urlpatterns = [

    path('', List_courses.as_view(), name = 'list_courses'), 
    path('search-course/', search_course_view, name = 'search_course_view'),
    path('course_detail/<int:pk>/', Detail_courses.as_view(), name = 'course_detail'),
    path('student_detail/<int:pk>/', student_detail, name = 'student_detail'),
    path('create_course/', Create_course.as_view(), name = 'create_course'),
    path('update_estudiante/', Update_student.as_view(), name = 'update_estudiante'),
]