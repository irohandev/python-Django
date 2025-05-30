# Importing Django's path and include functions to define URL patterns
from django.urls import path, include

# Importing view functions from the student app
from student.views import all_data, single_data

# List of URL patterns for the student app
urlpatterns = [
    # When the user goes to /all/, call the all_data view
    # URL name = 'all_data' (can be used in templates and redirects)
    path('all/', all_data, name='all_data'),

    # When the user goes to /single/, call the single_data view
    # URL name = 'single_data'
    path('single/', single_data, name='single_data'),
]
