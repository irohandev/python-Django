
from django.urls import path
from course.views import hello

urlpatterns = [
    path('hello/', hello, name='learn_django'),
]
