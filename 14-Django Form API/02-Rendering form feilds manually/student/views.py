# Importing the render function to render HTML templates
from django.shortcuts import render

from student.forms import Registration


# View function to handle the registration page
def registration(req):
    fm = Registration()
    return render(req, 'student/registration.html', {'form': fm})