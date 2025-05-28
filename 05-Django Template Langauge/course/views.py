from django.shortcuts import render
from datetime import datetime

def learn_django(request):
    # Variables (basic text)
    name = 'Django Framework'
    duration = '6 months complete full-stack course'
    seats = 25

    # List of students (for loop example)
    students = ['Aman', 'Priya', 'Suresh', 'Riya']

    # Dictionary (for loop with key-value example)
    course_info = {
        'course_name': 'Django Advanced',
        'teacher': 'Mr. Rahul',
        'mode': 'Online',
    }

    # Current date and time
    dt = datetime.now()

    # Float values
    p1 = 56.2345
    p2 = 100.0
    p3 = 45.6789

    # Empty and None values for testing filters
    empty_var = ''
    none_var = None

    # HTML injection for testing |safe filter
    html_content = "<strong>This is bold text</strong>"

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
    return render(request, 'course/django.html', context)
