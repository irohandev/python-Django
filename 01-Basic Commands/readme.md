# --------------------------------------------
# 🌐 1. Create & Activate Virtual Environment
# --------------------------------------------

# Install virtualenv (if not already installed)
pip install virtualenv

# Create virtual environment named 'venv'
virtualenv venv

# Activate virtual environment
# For Windows:
venv\Scripts\activate
# For macOS/Linux:
source venv/bin/activate


# ----------------------------
# 📦 2. Install Django
# ----------------------------
pip install django

# Check Django version
django-admin --version


# ----------------------------
# 🚀 3. Start a Django Project
# ----------------------------
django-admin startproject project_name

cd project_name


# ----------------------------
# 📱 4. Start a Django App
# ----------------------------
python manage.py startapp app_name

# Register the app in settings.py:
# INSTALLED_APPS = [
#     ...,
#     'app_name',
# ]


# ----------------------------
# 🧱 5. Run Migrations
# ----------------------------
# Create migration files for your models
python manage.py makemigrations

# Apply migrations to the database
python manage.py migrate

# Optional: See SQL for a migration
python manage.py sqlmigrate app_name 0001

# Show all migrations and their status
python manage.py showmigrations


# ----------------------------
# 👤 6. Create Superuser
# ----------------------------
python manage.py createsuperuser


# ----------------------------
# 🌐 7. Run Development Server
# ----------------------------
# Run on default port 8000
python manage.py runserver

# Run on custom port
python manage.py runserver 8080


# ----------------------------
# 🐚 8. Open Django Shell
# ----------------------------
python manage.py shell


# ----------------------------
# 🗃️ 9. Access DB Shell (if using SQLite)
# ----------------------------
python manage.py dbshell


# ----------------------------
# 🎨 10. Collect Static Files (Production)
# ----------------------------
python manage.py collectstatic


# ----------------------------
# ✅ 11. Run Tests (if any)
# ----------------------------
python manage.py test


# ----------------------------
# 🆘 12. Help Commands
# ----------------------------
# List all available Django commands
python manage.py help

# Help for a specific command
python manage.py help runserver


# ----------------------------
# 📦 13. Requirements File
# ----------------------------
# Freeze all installed packages to requirements.txt
pip freeze > requirements.txt


# ----------------------------
# 🟢 14. Deploy with Gunicorn (Production Server)
# ----------------------------
# Install Gunicorn
pip install gunicorn

# Run project using Gunicorn
gunicorn project_name.wsgi


# ----------------------------
# 🔴 15. Deactivate Virtual Environment
# ----------------------------
deactivate
