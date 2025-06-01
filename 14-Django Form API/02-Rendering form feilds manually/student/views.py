# Importing the render function to render HTML templates
from django.shortcuts import render

from student.forms import Registration, Address


# View function to handle the registration page
def registration(req):
    fm = Registration(auto_id=True, initial={'email': ''})
    return render(req, 'student/registration.html', {'form': fm})


def address(req):
    fm = Address()
    return render(req, 'student/address.html', {'form': fm})