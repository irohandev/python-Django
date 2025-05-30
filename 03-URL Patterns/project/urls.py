from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app_1.urls')),  # Include URLs from app_1
    path('app_2/', include('app_2.urls')),  # Include URLs from app_2 i.e localhost:3000/app_2/
]
