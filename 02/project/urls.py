"""Project URL Configuration"""

from django.contrib import admin
from django.urls import path
from app_1 import views  # Importing views from the app named 'app_1'

# from app_1.views import function_1  - we can do this also by importing the specific view function 'function_1' from 'app_1.views'


urlpatterns = [
    # This URL pattern is for the Django admin panel. It connects the '/admin/' route to the default Django admin interface.
    path('admin/', admin.site.urls),

    # In the path function:
    # - The first argument is the URL route (e.g., 'function_1/').
    # - The second argument is the view function that will handle the request when this URL is accessed (here, 'views.function_1').
    # - The third argument is an optional name for this URL pattern (here, 'name="function_1"'). It's useful for reverse URL resolution.
    # Only the route and view function are required. The 'name' parameter is optional and can be left out if not needed.
    path('function_1/', views.function_1, name='function_1'),  # Mapping the 'function_1/' route to the 'function_1' view
]
