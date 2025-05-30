from django.db import models  # Importing Django's built-in models module to create database models

# Create your models here.
# This model represents a user's profile with basic details
class Profile(models.Model):
    # 'name' will store the user's full name, max length set to 100 characters
    name = models.CharField(max_length=100)

    # 'email' will store the user's email address, with a max length of 200 characters
    email = models.EmailField(max_length=200)

    # 'city' will store the name of the user's city, max length set to 100 characters
    city = models.CharField(max_length=100)

    # 'roll' can store any kind of identifier (like roll number or ID), max length set to 100 characters
    roll = models.CharField(max_length=100)
