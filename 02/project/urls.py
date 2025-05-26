"""Project URL Configuration"""

from django.contrib import admin
from django.urls import path
from app_1 import views  # Importing views module from the app named 'app_1'

# Alternatively, we could import specific view functions directly:
# from app_1.views import function_1

urlpatterns = [
    # URL pattern for the Django admin interface.
    # It connects the URL path '/admin/' to Django's built-in admin site.
    path('admin/', admin.site.urls),

    # URL pattern mapping:
    # - 'function_1/' is the URL route.
    # - 'views.function_1' is the view function to handle requests to this route.
    # - {'status': 'OK'} is an optional dictionary of keyword arguments passed to the view.
    # - 'name' assigns a unique identifier to this URL pattern useful for reverse lookups.
    path('function_1/', views.function_1, {'status': 'OK'}, name='function_1'),

    # Another URL pattern for the same view function 'function_1',
    # but accessed via the route 'function_2/'.
    # Since no kwargs are passed here, the view will use default values.
    # This allows the same logic to be triggered by different URLs.
    path('function_2/', views.function_1, name='function_1'),
]
