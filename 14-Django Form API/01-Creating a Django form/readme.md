# Django Form API - README

This README provides a beginner-friendly guide to using Django's Form API, based on examples like Registration and Login forms.

## 📌 What is Django Form API?

Django's Form API allows developers to create, render, validate, and process HTML forms easily in Python. It supports built-in field validation, custom layouts, and integration with templates.

---

## 🛠️ Basic Setup

### 1. Create a Django App (if not done already)

```bash
python manage.py startapp student
```

### 2. Define Forms in `student/forms.py`

```python
from django import forms

class Registration(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.CharField()
    city = forms.CharField()

class Login(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())
```

---

## 🧠 Views - Handling Forms in `student/views.py`

```python
from django.shortcuts import render
from student.forms import Registration, Login

# Registration view
def registration(req):
    fm = Registration(field_order=['email', 'city', 'first_name', 'last_name'])
    return render(req, 'student/registration.html', {'form': fm})

# Login view
def login(req):
    fm = Login(initial={'email': 'rohan@gmaail.com'})
    return render(req, 'student/login.html', {'form': fm})
```

---

## 🖼️ Templates

### `registration.html`

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Registration</title>
</head>
<body>
    <h1>Student Registration</h1>
    <form action="" method="post">
        {% csrf_token %}
        {{ form }}
        <button type="submit">Submit</button>
    </form>
</body>
</html>
```

### `login.html`

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login</title>
</head>
<body>
    <h1>Login Page</h1>
    <form action="" method="post">
        {% csrf_token %}
        {{ form }}
        <input type="submit" value="Login">
    </form>
</body>
</html>
```

---

## ✅ Features Demonstrated

* `field_order` to change display order of fields
* `initial` to set pre-filled values
* `widget=forms.PasswordInput()` to mask password input
* Automatic rendering with `{{ form }}`

---

## 🔐 Note on Security

Always include `{% csrf_token %}` inside form tags when using POST method to protect against CSRF attacks.

---

## 📚 Additional Tips

* You can use `{{ form.as_p }}`, `{{ form.as_table }}`, or `{{ form.as_ul }}` for structured rendering.
* To access individual fields: `{{ form.email }}`, `{{ form.password }}` etc.
* Add custom validation by defining `clean_<fieldname>()` methods inside the form class.

---

## 📂 Folder Structure Example

```
project/
    student/
        forms.py
        views.py
        templates/
            student/
                registration.html
                login.html
```

---

Use this setup to build user-friendly forms quickly with Django's powerful Form API!
