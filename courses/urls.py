
from django.urls import path

from courses.views import *


urlpatterns = [

    path('', courses, name = 'courses') ]