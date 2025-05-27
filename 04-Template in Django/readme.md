
# Django Template -

The goal of this project is to demonstrate how to render HTML pages using Django's **template system** instead of returning raw HTML via `HttpResponse` in views. This makes the application more scalable, maintainable, and organized.

---

## Folder Structure

Make sure your Django app follows this structure:

```
your_project/
│
├── your_app/
│   ├── views.py
│   ├── templates/
│   │   └── your_app/
│   │       └── django.html
│   └── ...
│
└── manage.py
```

---

## 🔧 Step-by-Step Setup

### 1. Create Templates Folder

Inside your Django app (`your_app`), create a folder named `templates`. Inside that, create another folder with the **same name as your app**. Place all your HTML files in this nested folder.

### 2. Create the HTML File

Path: `your_app/templates/your_app/django.html`

```html
<!DOCTYPE html>
<html>
<head>
    <title>Django Template</title>
</head>
<body>
    <h1>Welcome to Django Template Rendering</h1>
</body>
</html>
```

### 3. Update Your View

In your `views.py`, use Django's `render()` function instead of `HttpResponse`:

```python
from django.shortcuts import render

def my_view(request):
    return render(request, 'your_app/django.html')
```

---

## Why Use Templates?

- ✅ **Separation of Concerns**: Keeps business logic and HTML separate.
- ✅ **Reusability**: Templates can be reused across multiple views.
- ✅ **Maintainability**: Cleaner code that's easier to manage and scale.
- ✅ **Dynamic Rendering**: You can pass context data to templates.

---

##  Bonus: Passing Dynamic Data

If you want to send variables from your view to the template:

### View (views.py):

```python
def my_view(request):
    context = {'name': 'Aman'}
    return render(request, 'your_app/django.html', context)
```

### Template (django.html):

```html
<h1>Hello {{ name }}</h1>
```

---

## Conclusion

Using Django's template rendering system improves your application's structure and maintainability. It is the preferred approach for any real-world or production-level Django project.

---

