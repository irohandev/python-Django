from django.contrib import admin
from django.urls import path
from app_2.views import myapp2


urlpatterns = [
    path('admin/', admin.site.urls),
    path('app_2/', myapp2, name='myapp2'),
]
