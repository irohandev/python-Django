from django.urls import path
from course.views import learn_Django, learn_Django_template


urlpatterns = [
    path('dj/' , learn_Django, name='learn_django'),
    path('dj_template/', learn_Django_template, name='learn_django_template'),
]
