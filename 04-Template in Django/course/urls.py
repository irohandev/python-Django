from django.urls import path
from course.views import learn_Django


urlpatterns = [
    path('dj/' , learn_Django, name='learn_django'),
]
