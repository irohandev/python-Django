from django.shortcuts import render
from datetime import datetime

def learn_django(request):
    # Basic text variables to display on the HTML page
    name = 'Django Framework'
    duration = '6 months complete full-stack course'
    seats = 25

    # List of students for demonstrating the 'for' loop in templates
    students = ['Aman', 'Priya', 'Suresh', 'Riya']

    # Dictionary for demonstrating key-value looping in templates
    course_info = {
        'course_name': 'Django Advanced',
        'teacher': 'Mr. Rahul',
        'mode': 'Online',
    }

    # Current date and time to demonstrate date/time filters in templates
    dt = datetime.now()

    # Float values to demonstrate floatformat filter
    p1 = 56.2345
    p2 = 100.0
    p3 = 45.6789

    # Empty string and None value to demonstrate default/default_if_none filters
    empty_var = ''
    none_var = None

    # HTML content string to demonstrate safe filter (prevents auto-escaping)
    html_content = "<strong>This is bold text</strong>"

    # Dictionary that passes all variables to the HTML template
    context = {
        'name': name,
        'duration': duration,
        'seats': seats,
        'students': students,
        'course_info': course_info,
        'dt': dt,
        'p1': p1,
        'p2': p2,
        'p3': p3,
        'empty_var': empty_var,
        'none_var': none_var,
        'html_content': html_content,
    }

    # Render the HTML template with the context data
    return render(request, 'course/django.html', context)
