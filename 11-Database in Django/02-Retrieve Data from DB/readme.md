## 🧠 Django Models & Database Migration Guide

### 🔧 What are Models?

In Django, **models** are Python classes that represent database tables. Each class corresponds to a table, and its attributes (fields) represent the columns in that table.

#### 📌 Example:

```python
# models.py

from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    roll_number = models.IntegerField(unique=True)
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
```

Explanation:

* `CharField`, `IntegerField`, `EmailField` represent fields that will become SQL table columns.
* `auto_now_add=True` automatically stores the creation timestamp.

---

### 🦁 What are Migrations?

Migrations are how Django propagates changes made to models (like adding a field or changing a field type) into your database schema.

Django automatically generates migration files (inside the `migrations/` folder) based on changes in your models, and you then apply these changes to your database.

---

### 📁 Important Notes:

* The `__str__` method makes objects readable and user-friendly in Django admin.
* Whenever you make any changes to a model (add/remove/rename fields):

  * Run `makemigrations`
  * Then run `migrate`

---

## 📚 Example Flow:

1. Add the `Student` class in `models.py`.
2. Run the following commands step-by-step:

```bash
# Detect model changes and create a migration file
python manage.py makemigrations

# Apply the migration to the database
python manage.py migrate

# Make migrations for a specific app
python manage.py makemigrations your_app_name

# Show the status of migrations
python manage.py showmigrations

# Roll back to a specific migration number
python manage.py migrate your_app_name 000X
```

> 🔁 Replace `your_app_name` with the name of your Django app and `000X` with the migration number you want to roll back to.

3. A table named `yourapp_student` will be created in the database.

---

## 📄 Retrieving Data in Django (Template Based)

There are multiple ways to retrieve and display data from the database in Django views and templates.

### 1. Basic View and Template

#### ✅ views.py

```python
from django.shortcuts import render
from .models import Student

def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})
```

#### ✅ student\_list.html

```html
<h2>All Students</h2>
<ul>
  {% for student in students %}
    <li>{{ student.name }} - {{ student.roll_number }}</li>
  {% endfor %}
</ul>
```

---

### 2. Filtered Query

```python
students = Student.objects.filter(name__icontains='john')
```

Displays students whose name contains "john" (case-insensitive).

---

### 3. Single Object

```python
student = Student.objects.get(pk=1)  # get student with primary key 1
```

---

### 4. Using QuerySet in Template

```html
{% for student in students %}
  <p>{{ student.name }} | {{ student.email }}</p>
{% endfor %}
```

---

### 5. Custom Order or Slicing

```python
students = Student.objects.all().order_by('-created_at')[:5]  # latest 5 entries
```

---

You can mix filters, conditions, ordering etc. inside your views and then pass that QuerySet to any Django template for display.
