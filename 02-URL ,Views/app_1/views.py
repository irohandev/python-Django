from django.shortcuts import render

# Import HttpResponse to send HTTP responses back to the user
from django.http import HttpResponse            

# This is a standard Python function that takes a request and returns a response.
# To make this function accessible via a URL, we need to add it to the project's urls.py file.
# This means importing the function there and defining a URL route for it.

def function_1(request, **kwargs):
    # Get the 'status' value from kwargs, defaulting to the string '200' if not provided
    status = kwargs.get('status', '200')
    
    try:
        # Attempt to convert the status to an integer to use as the HTTP status code
        status_code = int(status)
    except ValueError:
        # If conversion fails, default the status code to 200 (OK)
        # Note: status_code must be an integer; strings are not accepted
        status_code = 200
    
    # Prepare the response text including the status information
    response_text = f"Hello, this is function_1 from app_1 views.py. Status: {status}"
    
    # Return an HttpResponse with the response text and the HTTP status code
    return HttpResponse(response_text, status=status_code)
