# 🌐 Django Static Files Guide (CSS, JS, Images)

This project demonstrates how to properly use **static files** like CSS, JavaScript, and Images inside Django templates.

---

## 📁 Project Structure (Relevant Parts)

```
course/
├── static/
│   └── course/
│       ├── css/
        |   └── style.css
│       ├── js/
        |   └── script.js
│       └── images/
│           └── img.jpg
├── templates/
│   └── course/
│       └── dj_django.html
```

---

## ⚙️ 1. Static Files Configuration in `settings.py`

Ensure the following lines are present in your Django `settings.py`:

```python
STATIC_URL = '/static/'

# (Optional for development if you want to serve additional static directories)
# STATICFILES_DIRS = [BASE_DIR / "static"]
```

---

## 📌 2. Using Static Files in Templates

### Step 1: Load the static tag

At the **top** of your HTML template (`dj_django.html`):

```django
{% load static %}
```

### Step 2: Use Static Files in HTML

#### ✅ Link a CSS file

```html
<link rel="stylesheet" href="{% static 'course/css/style.css' %}">
```

#### ✅ Link a JS file

```html
<script src="{% static 'course/js/script.js' %}"></script>
```

#### ✅ Use an Image

```html
<img src="{% static 'course/images/img.jpg' %}" alt="My Image">
```

---

## 📝 3. Notes

* Organize static files using subfolders: `css`, `js`, `images`.
* Use app name (`course/`) as a namespace to avoid conflicts in larger projects.
* Never hardcode paths like `/static/...` directly. Always use `{% static %}` for reliability across environments.
* To check if static files are loading properly, use browser DevTools (F12 → Network Tab).

---

## ✅ Example Template (`dj_django.html`)

```html
{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Django Static Example</title>
    <link rel="stylesheet" href="{% static 'course/css/style.css' %}">
</head>
<body>
    <h1>Hello from Django Template</h1>
    <img src="{% static 'course/images/img.jpg' %}" alt="Example Image">
</body>
</html>
```
