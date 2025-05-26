from django.shortcuts import render

# First, we need to import HttpResponse to be able to send an HTTP response back to the user.
from django.http import HttpResponse            

# This is a normal Python function that takes a request and returns a response.
# To display the output of this function when someone visits a specific route,
# we need to add this function to the project's urls.py file.
# That means we have to import this function there and define its route.
def function_1(request):
    return HttpResponse("Hello, this is function_1 from app_1 views.py")
