
from django.urls import path

from courses.views import *


urlpatterns = [

    path('', courses, name = 'courses'), 
    path('search-course/', search_course_view, name = 'search_course_view') 
    
    
]