from django.shortcuts import render
from courses.models import *


# Create your views here.
def courses(request):
    new_course = Courses.objects.create(
    name = 'Ruby', 
    price = 1666, 
    description = 'OLD AF', 
    student_qty = 42,
    difficulty_hard = True
    
     )

    context = {'new_course': new_course}
    return render(request, 'courses.html', context = context)

