
# 🧰 Django Basic guide !

A complete guide to using Django – the high-level Python Web framework that promotes rapid development and clean, pragmatic design.

---

## 📚 Table of Contents

- [What is Django?](#what-is-django)
- [Installation](#installation)
- [Project Setup](#project-setup)
- [Creating an App](#creating-an-app)
- [URL Routing](#url-routing)
- [Views and Templates](#views-and-templates)
- [Models and Migrations](#models-and-migrations)
- [Django Admin](#django-admin)
- [Handling Forms](#handling-forms)
- [Django ORM Queries](#django-orm-queries)
- [Authentication](#authentication)
- [Static and Media Files](#static-and-media-files)
- [Django Commands](#django-commands)
- [REST API (Django REST Framework)](#rest-api-django-rest-framework)
- [Real-World Use Cases](#real-world-use-cases)

---

## 📌 What is Django?

**Django** is a powerful web framework written in Python that encourages rapid development and clean design.

> "Django makes it easier to build better web apps more quickly and with less code."

---

## ⚙️ Installation

Install Django using `pip`:

```bash
pip install django
```

---

## 🚀 Project Setup

### ✅ Start a New Project:
```bash
django-admin startproject myproject
cd myproject
python manage.py runserver
```

### ✅ Project Directory Structure:
```
myproject/
├── manage.py
└── myproject/
    ├── __init__.py
    ├── settings.py
    ├── urls.py
    ├── asgi.py
    └── wsgi.py
```

---

## 🧩 Creating an App

Apps are components within a Django project.

```bash
python manage.py startapp myapp
```

Add your app to `INSTALLED_APPS` in `settings.py`:
```python
INSTALLED_APPS = [
    'myapp',
    ...
]
```

---

## 🌐 URL Routing

### ✅ Project-level `urls.py`:
```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),
]
```

### ✅ App-level `urls.py`:
Create `urls.py` in the app folder:
```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
]
```

---

## 👁️ Views and Templates

### ✅ `views.py`:
```python
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')
```

### ✅ Template File (`home.html`):
Create a folder `templates` and a file inside it:
```html
<!DOCTYPE html>
<html>
<head><title>Home</title></head>
<body>
    <h1>Hello from Django!</h1>
</body>
</html>
```

### ✅ Update Template Settings in `settings.py`:
```python
'DIRS': [BASE_DIR / 'templates'],
```

---

## 🧱 Models and Migrations

### ✅ models.py:
```python
from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    roll_no = models.IntegerField()
    email = models.EmailField()
```

### ✅ Migrate:
```bash
python manage.py makemigrations
python manage.py migrate
```

---

## 🧑‍💼 Django Admin

### ✅ Create a Superuser:
```bash
python manage.py createsuperuser
```

### ✅ Register your Model in `admin.py`:
```python
from .models import Student
admin.site.register(Student)
```

Visit: http://127.0.0.1:8000/admin/

---

## 📝 Handling Forms

### ✅ View:
```python
def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
    return render(request, 'contact.html')
```

### ✅ Template:
```html
<form method="POST">
    {% csrf_token %}
    <input type="text" name="name">
    <button type="submit">Submit</button>
</form>
```

---

## 🧠 Django ORM Queries

| Operation | Example |
|----------|---------|
| Create | `Student.objects.create(name="Aman")` |
| Read | `Student.objects.all()` |
| Filter | `Student.objects.filter(name="Aman")` |
| Get One | `Student.objects.get(id=1)` |
| Update | `Student.objects.filter(id=1).update(name="New")` |
| Delete | `Student.objects.get(id=1).delete()` |

---

## 🔐 Authentication

### ✅ Login View:
```python
from django.contrib.auth import authenticate, login

def login_user(request):
    user = authenticate(username='admin', password='1234')
    if user:
        login(request, user)
```

### ✅ Protected View:
```python
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')
```

---

## 🖼️ Static and Media Files

### ✅ settings.py:
```python
STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
```

### ✅ urls.py:
```python
from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

---

## 🛠️ Django Commands

| Command | Description |
|--------|-------------|
| `runserver` | Start development server |
| `makemigrations` | Create migration files |
| `migrate` | Apply migrations |
| `createsuperuser` | Create admin user |
| `shell` | Launch interactive shell |
| `collectstatic` | Collect static files for production |

---

## 🔌 REST API (Django REST Framework)

### ✅ Install:
```bash
pip install djangorestframework
```

### ✅ Add to settings:
```python
INSTALLED_APPS = ['rest_framework']
```

### ✅ Sample API View:
```python
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def api_home(request):
    return Response({"message": "Hello from API!"})
```

---

## 🏢 Real-World Use Cases

- Blog engines
- E-commerce stores
- Admin dashboards
- APIs and mobile app backends
- Learning Management Systems
- CRM / ERP systems

---

## ✅ Conclusion

Django is a robust, versatile, and beginner-friendly framework. Whether you're building a simple blog or a full-featured enterprise application, Django gives you the tools to build it quickly, securely, and beautifully.

> Feel free to fork this guide or contribute to make it even better!
