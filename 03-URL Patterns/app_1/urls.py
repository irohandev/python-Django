from django.urls import path
from app_1.views import function_1

urlpatterns = [
    path('function_1/', function_1, {'status': 'OK'}, name='function_1'),
    path('function_2/', function_1, name='function_1'),

]
