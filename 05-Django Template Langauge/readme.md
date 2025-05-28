# Django Template Tags & Filters Showcase

This Django project is a complete guide for understanding how to use **Django Template Tags and Filters**. It demonstrates the usage of variables, filters (like `upper`, `lower`, `truncatewords`, `date`, `floatformat`, etc.), conditional statements, loops, safe HTML rendering, and much more.

---

## 🧠 What This Project Covers

* Passing data from views to templates
* Using variables, conditionals (`if`/`else`)
* Looping over lists and dictionaries
* Template filters (`upper`, `lower`, `truncate`, `floatformat`, `date`, etc.)
* Handling empty or None values with `default`, `default_if_none`
* Rendering HTML safely using the `safe` filter
* Escaping and unescaping content with `{% autoescape %}`

---

## 📂 Project Structure

```
django_project/
│
├── course/
│   ├── templates/
│   │   └── course/
│   │       └── django.html      # Template file with all filters and tags
│   └── views.py                 # Django view sending context data
│
├── django_project/
│   └── settings.py              # Basic project configuration
│
├── manage.py
└── README.md
```


