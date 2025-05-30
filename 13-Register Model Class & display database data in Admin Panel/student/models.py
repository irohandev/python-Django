from django.db import models
# Importing Django's models module to create database tables

# Create your models here.

# Defining the Profile model to store student details
class Profile(models.Model):
    # Student's name, max length 100 characters
    name = models.CharField(max_length=100)
    # Student's roll number as an integer
    roll = models.IntegerField()
    # Student's email address, max length 100 characters
    email = models.EmailField(max_length=100)
    # City where the student lives, max length 100 characters
    city = models.CharField(max_length=100)

    # Uncomment this method to display the email when printing the object
    # def __str__(self):
    #     return self.email

# Defining the Result model to store student marks
class Result(models.Model):
    # The class/grade of the student
    stu_class = models.CharField(max_length=100)
    # Marks obtained by the student as an integer
    marks = models.IntegerField()
