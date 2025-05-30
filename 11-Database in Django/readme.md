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
