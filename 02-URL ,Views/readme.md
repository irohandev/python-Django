## Step-by-Step Setup Process

### 1. Install Django and Create Project
After installing Django, create a new project:

```bash
django-admin startproject project_name
cd project_name
```

---

### 2. Create Django App
Create a new app in your project:

```bash
python manage.py startapp app_name
```

---

### 3. Add App to INSTALLED_APPS
Go to your project's `settings.py` file and add your app:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app_name',  # Add your app name here
]
```

---

### 4. Create Views
In your app's `views.py` file, first import HttpResponse:

```python
from django.http import HttpResponse

def your_function_name(request):
    return HttpResponse("Hello, World!")
```

---

### 5. Configure URLs
In your main project's `urls.py` file:

```python
from django.contrib import admin
from django.urls import path
from app_name import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('route/', views.your_function_name, name='function_name'),
]
```

Each path needs: route, view function, and name.

---

### 6. Run Server
```bash
python manage.py runserver
```

Now visit your route to see the function response!