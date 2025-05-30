from django.contrib import admin
# Importing Django's admin module to register models for the admin interface

from student.models import Profile, Result
# Importing the Profile and Result models from the student app

# Register your models here.

# Customizing the admin interface for Profile model
class ProfileAdmin(admin.ModelAdmin):
    # Specifies the fields to display in the admin list view for Profile
    list_display = ('name', 'roll', 'city')

# Registering the Profile model with the customized ProfileAdmin
admin.site.register(Profile, ProfileAdmin)
# Registering the Result model with default admin options
admin.site.register(Result)
