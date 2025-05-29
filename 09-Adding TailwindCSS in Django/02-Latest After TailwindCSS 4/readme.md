# Using Tailwind CSS v4 with Django (Updated Guide)

This README provides an updated and simplified guide for using Tailwind CSS v4 in a Django project **without relying on `django-tailwind`**. Instead, we’ll use the official Tailwind CLI and integrate it with your Django templates manually. This is the most flexible and up-to-date method to use Tailwind v4+.

---

## Prerequisites

* Python 3.8+
* Django 4.0 or later
* Node.js and npm installed

---

## Step 1: Setup Django Project (If not already)

If you haven't already created a Django project:

```bash
django-admin startproject myproject
cd myproject
python manage.py startapp core
```

---

## Step 2: Install Tailwind CSS via CLI

Install Tailwind globally or as a dev dependency in your frontend folder:

```bash
npm create tailwind@latest frontend
cd frontend
npm install
```

Choose a template (`empty`, `with play`, etc.) when prompted. The Tailwind CLI will scaffold the folder.

---

## Step 3: Tailwind Config

Update the `tailwind.config.js` file to include Django template paths:

```js
/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    '../**/templates/**/*.html',
    '../**/templates/*.html',
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}
```

---

## Step 4: Add Input CSS

Edit or create `src/input.css` in the `frontend/` folder:

```css
@tailwind base;
@tailwind components;
@tailwind utilities;
```

---

## Step 5: Build Tailwind CSS

Build the output CSS manually using Tailwind CLI:

```bash
npx tailwindcss -i ./src/input.css -o ./static/css/styles.css --watch
```

Make sure the `static/css/styles.css` path exists. Adjust the output path to your Django static folder.

---

## Step 6: Serve Static Files in Django

In `settings.py`, configure static files:

```python
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'frontend/static']
```

---

## Step 7: Load CSS in Django Templates

In your base Django HTML file (e.g., `base.html`):

```html
{% load static %}
<link rel="stylesheet" href="{% static 'css/styles.css' %}">
```

---

## Step 8: Run Everything

Start Tailwind watcher (for auto CSS rebuilds):

```bash
cd frontend
npx tailwindcss -i ./src/input.css -o ./static/css/styles.css --watch
```

In a second terminal, run Django:

```bash
python manage.py runserver
```

Now you can use Tailwind classes in your Django templates.

---

## Optional: Browser Reload (Dev Only)

Install `django-browser-reload` for auto-refresh:

```bash
pip install django-browser-reload
```

Add to `INSTALLED_APPS`, `MIDDLEWARE`, and `urls.py` as usual.

---

## Recommended Project Structure

```
myproject/
├── frontend/
│   ├── src/input.css
│   ├── static/css/styles.css
│   ├── tailwind.config.js
│   └── package.json
├── core/
│   └── templates/
│       └── base.html
├── myproject/
│   └── settings.py
```

---

## Summary

* Use Tailwind CSS v4 directly via CLI for the latest features.
* Tailwind CSS builds static CSS which Django serves normally.
* You gain full control over your frontend and faster build times without extra Django packages.

This approach is modern, simple, and future-proof for integrating Tailwind with Django.
