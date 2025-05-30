# Registering and Displaying Models in Django Admin Panel

This guide explains how to define models in Django, register them with the admin site, and customize their display to show specific data in the Django admin panel.

## Prerequisites

* A Django project is already set up
* An app has been created using `python manage.py startapp your_app_name`
* The admin panel and a superuser account are properly configured

## Step 1: Define Your Models

Open the `models.py` file in your Django app and define your models using Django's ORM syntax. Example:

```python
from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length=100)
    roll = models.IntegerField()
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Result(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    marks = models.IntegerField()

    def __str__(self):
        return f"{self.profile.name} - {self.subject}"
```

> The `__str__` method helps display readable object names in the admin interface.

## Step 2: Apply Migrations

Run the following commands to create and apply the necessary database migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

## Step 3: Register Models in the Admin Panel

To make models visible in the Django admin interface, register them in your app’s `admin.py` file.

```python
from django.contrib import admin
from student.models import Profile, Result

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'roll', 'city')  # Fields to show in admin list view

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Result)
```

* `list_display` is used to specify which fields should be shown in the list view of the admin panel.
* You can also customize search, filtering, and ordering behavior using other options like `search_fields`, `list_filter`, and `ordering`.

## Step 4: View and Manage Data in the Admin Panel

1. Start the development server:

   ```bash
   python manage.py runserver
   ```

2. Open your browser and go to:

   ```
   http://127.0.0.1:8000/admin/
   ```

3. Log in using your superuser credentials.

4. Under your app's name, you will see the `Profile` and `Result` models.

5. Click on a model to view, add, edit, or delete its records.

## Conclusion

Django's admin panel is a powerful tool for managing application data without the need for a separate interface. By defining models and registering them with customization options like `list_display`, you can control exactly how data is presented and accessed by administrators.

For more advanced configurations, explore inline models, admin filters, and custom actions to enhance the functionality of the admin panel.
