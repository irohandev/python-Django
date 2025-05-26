# Django Commands Reference

## 🌐 Virtual Environment
```bash
# Install virtualenv
pip install virtualenv

# Create virtual environment
virtualenv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Deactivate virtual environment
deactivate
```

## 📦 Django Installation
```bash
# Install Django
pip install django

# Check Django version
django-admin --version
```

## 🚀 Project & App Creation
```bash
# Create Django project
django-admin startproject project_name
cd project_name

# Create Django app
python manage.py startapp app_name
```

## 🧱 Database Commands
```bash
# Create migration files
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# View SQL for migration
python manage.py sqlmigrate app_name 0001

# Show migration status
python manage.py showmigrations
```

## 👤 User Management
```bash
# Create superuser
python manage.py createsuperuser
```

## 🌐 Server Commands
```bash
# Run development server (default port 8000)
python manage.py runserver

# Run on custom port
python manage.py runserver 8080
```

## 🐚 Shell & Database
```bash
# Open Django shell
python manage.py shell

# Open database shell
python manage.py dbshell
```

## 🎨 Static Files
```bash
# Collect static files
python manage.py collectstatic
```

## ✅ Testing
```bash
# Run all tests
python manage.py test

# Run specific app tests
python manage.py test app_name
```

## 🆘 Help Commands
```bash
# List all Django commands
python manage.py help

# Help for specific command
python manage.py help runserver
```

## 📦 Requirements
```bash
# Create requirements file
pip freeze > requirements.txt

# Install from requirements
pip install -r requirements.txt
```

## 🟢 Production (Gunicorn)
```bash
# Install Gunicorn
pip install gunicorn

# Run with Gunicorn
gunicorn project_name.wsgi

# Run with custom bind
gunicorn project_name.wsgi --bind 0.0.0.0:8000
```