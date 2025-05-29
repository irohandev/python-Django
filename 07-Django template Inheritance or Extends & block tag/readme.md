# Django Template Inheritance (`extends` and `block`)

Django template inheritance is a powerful feature that helps you avoid repeating common HTML structures like headers, footers, and navigation menus across different pages. Instead of rewriting these parts in every template, you can define them once in a base template (e.g., `base.html`) and extend this in your other templates.

## How Does Template Inheritance Work?

* **`{% extends "base.html" %}`**: This tells Django that the current template inherits from `base.html`. The base template provides the structure.
* **`{% block blockname %}...{% endblock %}`**: These are placeholders defined in the base template. Child templates can fill or override these blocks with custom content.

## 1. Create a `base.html` File

This is the main layout template that other templates will extend.

```html
<!-- templates/base.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{% block title %}My Website{% endblock %}</title>
</head>
<body>
    <header>
        <h1>Welcome to My Website</h1>
    </header>

    <nav>
        <!-- Navigation links -->
    </nav>

    <main>
        {% block content %}
        <!-- Default content -->
        {% endblock %}
    </main>

    <footer>
        <p>&copy; 2025 My Website</p>
    </footer>
</body>
</html>
```

## 2. Create a Child Template that Extends `base.html`

Now you can create a new template (e.g., `home.html`) that extends `base.html`. You only override the blocks where you want to change the content.

```html
<!-- templates/home.html -->
{% extends "base.html" %}

{% block title %}Home - My Website{% endblock %}

{% block content %}
<h2>Home Page</h2>
<p>This is the content of the home page.</p>
{% endblock %}
```

## 3. Rendering the Template in Views

Make sure to render the correct template from your Django view:

```python
# views.py
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')
```

## Summary

* Use `{% extends "base.html" %}` to inherit a base layout.
* Define reusable content areas using `{% block blockname %}` and `{% endblock %}`.
* Only override the necessary blocks in child templates.

### Benefits:

* Centralized layout for easier updates
* Cleaner and more maintainable code
* Structured and scalable web pages
