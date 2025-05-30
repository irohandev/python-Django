# Importing the render function to render HTML templates with context data
from django.shortcuts import render

# Importing the Profile model from the 'student' app's models.py
from student.models import Profile


# View function to display all student records
def all_data(req):
    # Fetching all records from the Profile table using Django ORM
    all_students = Profile.objects.all()

    # Rendering the 'student/all.html' template and passing all_students data
    return render(req, 'student/all.html', {'students': all_students})


# View function to display a single student record
def single_data(req):
    # Option 1: Get a student by primary key 
    # students = Profile.objects.get(pk=1)

    # Option 2: Get a student by id field 
    # students = Profile.objects.get(id=1)

    # Option 3 (used here): Get a student by name (name='Rohan')
    students = Profile.objects.get(name='Rohan')

    # Rendering the 'student/single.html' template and passing the single student data
    return render(req, 'student/single.html', {'student': students})
