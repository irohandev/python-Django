from django.urls import path
from student.views import registration, address

urlpatterns = [
    path('register/', registration, name='registration'),
    path('address/', address, name='address'),
]
