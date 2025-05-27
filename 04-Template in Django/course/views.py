# Importing the render function to render HTML templates
from django.shortcuts import render

# Importing HttpResponse to return raw HTML content directly (not ideal for dynamic content)
from django.http import HttpResponse

# This view function handles incoming requests for a specific route
def learn_Django(req):
    # Business Logic: Performing a simple calculation
    sum = 10 + 20

    # Presentation Logic: Manually creating an HTML response as a string
    html_content = f'<h1>Hello Django from course app!</h1><p>Sum is: {sum}</p>'

    # Returning the HTML content using HttpResponse (not recommended for large or dynamic pages)
    return HttpResponse(html_content)


# ---------------- Improved Approach Using Template Rendering ----------------

# Instead of manually writing HTML inside the view, we use Django’s render() function.
# This method loads an external HTML template and injects dynamic data into it.
# It is more efficient, cleaner, and easier to maintain.

def learn_Django_template(req):
    # Presentation Logic: Rendering an HTML template located at 'templates/course/django.html'
    return render(req, template_name='course/django.html')


# This view function demonstrates how to pass context data (dynamic variables) to templates
def greet(req):
    # Creating a context dictionary with dynamic data to send to the template
    fullname = {
        'fname': 'Rohan Dev Singh',
    }

    # Rendering the template 'course/greet.html' with the context data
    return render(req, template_name='course/greet.html', context=fullname)
