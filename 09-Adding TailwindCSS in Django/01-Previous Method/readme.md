# Installing Tailwind CSS in a Django Project (Full Guide)

This README provides a comprehensive step-by-step guide to installing and integrating Tailwind CSS into a Django project using the `django-tailwind` package. Tailwind CSS is a utility-first CSS framework that allows for rapid UI development directly within your HTML templates.

---

## Prerequisites

* Python 3.6+
* Django 3.2 or later
* Node.js and npm installed
* A running Django project

---

## Step 1: Install Required Python Packages

Install `django-tailwind` and optionally `django-browser-reload` for live reloading in development.

```bash
pip install django-tailwind django-browser-reload
```

---

## Step 2: Add to Installed Apps

In your `settings.py`, add the following to `INSTALLED_APPS`:

```python
INSTALLED_APPS = [
    ...
    'tailwind',
    'theme',  # your Tailwind app, name it anything
    'django_browser_reload',  # for auto browser refresh during development
]
```

Also add this middleware:

```python
MIDDLEWARE = [
    ...
    'django_browser_reload.middleware.BrowserReloadMiddleware',
]
```

And in your root `urls.py`:

```python
from django.urls import path, include

urlpatterns = [
    ...
    path("__reload__/, include("django_browser_reload.urls")),
]
```

---

## Step 3: Initialize Tailwind App

Generate a new app that will serve as the Tailwind theme:

```bash
python manage.py tailwind init theme
```

This creates a `theme` app with Tailwind configuration.

---

## Step 4: Tailwind App Configuration

Add these settings to `settings.py`:

```python
TAILWIND_APP_NAME = 'theme'
INTERNAL_IPS = [
    "127.0.0.1",
]
```

---

## Step 5: Install Node Dependencies

Navigate to the new `theme` app and install Tailwind dependencies:

```bash
cd theme
npm install
```

This installs Tailwind and other required frontend tooling.

---

## Step 6: Add Tailwind CSS to Input File

Edit `theme/static_src/input.css`:

```css
@tailwind base;
@tailwind components;
@tailwind utilities;
```

Edit `tailwind.config.js` to configure paths and customize your Tailwind build:

```js
module.exports = {
  content: [
    '../templates/**/*.html',
    '../../templates/**/*.html',
    './templates/**/*.html',
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}
```

---

## Step 7: Include Compiled CSS in Templates

Add this to your base template (`base.html`):

```html
{% load static %}
<link href="{% static 'css/dist/styles.css' %}" rel="stylesheet">
```

If using `django_browser_reload`, also add this in `<body>`:

```html
{% if debug %}{% include 'django_browser_reload/script.html' %}{% endif %}
```

---

## Step 8: Run Tailwind and Development Server

In one terminal, start the Tailwind watcher:

```bash
python manage.py tailwind start
```

In another terminal, run the Django dev server:

```bash
python manage.py runserver
```

---

## Step 9: Build CSS for Production

When you’re ready to deploy, run:

```bash
python manage.py tailwind build
```

This will generate an optimized CSS build in `theme/static/css/dist/styles.css`.

---

## Project Structure Example

```
myproject/
├── theme/
│   ├── static/
│   │   └── css/dist/styles.css
│   ├── static_src/
│   │   └── input.css
│   ├── templates/
│   ├── tailwind.config.js
│   └── package.json
├── templates/
│   └── base.html
├── myproject/
│   └── settings.py
```

---

## Summary

* `django-tailwind` simplifies integrating Tailwind with Django.
* Customize your Tailwind config and use classes directly in Django templates.
* Use `tailwind start` during development and `tailwind build` before deployment.
* `django-browser-reload` adds live browser reloading for easier styling.

With this setup, you can build modern, responsive, and highly customizable user interfaces using Tailwind CSS within Django.
