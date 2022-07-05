
from django.urls import path

from courses.views import *
from users.views import List_profiles

urlpatterns = [

    path('', List_courses.as_view(), name = 'list_courses'), 
    path('search-course/', search_course_view, name = 'search_course_view'),
    path('course_detail/<int:pk>/', Detail_courses.as_view(), name = 'course_detail'),
    path('update_course/<int:pk>/', Update_course.as_view(), name = 'update_course'),
    path('student_detail/<int:pk>/', student_detail, name = 'student_detail'),
    path('create_course/', Create_course.as_view(), name = 'create_course'),
    
    path('login/', login_view, name = 'login'),
    path('logout/', logout_view, name = 'logout'),
    path('register/', register_view, name = 'register'),
    path('delete_course/<int:pk>/', Delete_course.as_view(), name = 'delete_course'),
    
]