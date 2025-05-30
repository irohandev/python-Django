# Importing Django's base Model class and field types
from django.db import models

# Defining a model named 'Profile' to represent student data in the database
class Profile(models.Model):
    # 'name' field to store the student's full name
    # CharField is used for short text with a maximum length of 100 characters
    name = models.CharField(max_length=100)

    # 'email' field to store the student's email address
    # EmailField automatically validates proper email format
    email = models.EmailField(max_length=200)

    # 'city' field to store the student's city
    # CharField again, with a max length of 100
    city = models.CharField(max_length=100)
