
from django.urls import path

from courses.views import *


urlpatterns = [

    path('',courses, name = 'courses'), 
    path('search-course/', search_course_view, name = 'search_course_view'),
    path('course_detail/<int:pk>/', course_detail, name = 'course_detail'),
    path('student_detail/<int:pk>/', student_detail, name = 'student_detail'),
    
    
]