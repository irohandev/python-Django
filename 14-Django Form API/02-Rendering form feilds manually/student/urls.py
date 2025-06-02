# Importing the `path` function to define URL patterns
from django.urls import path

# Importing the view functions `registration` and `address` from the `student.views` module
from student.views import registration, address

# List of URL patterns for routing
urlpatterns = [
    # When the user visits the URL ending in 'register/', call the `registration` view
    # This is typically used for handling student registration logic
    path('register/', registration, name='registration'),

    # When the user visits the URL ending in 'address/', call the `address` view
    # This view might be used to show or submit a student's address
    path('address/', address, name='address'),
]
