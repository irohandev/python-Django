# Importing the render function to render HTML templates
from django.shortcuts import render

# Importing the custom Registration and Login form classes from student/forms.py
from student.forms import Registration, Login


# View function to handle the registration page
def registration(req):
    # Creating a form instance with a custom field order
    # This reorders the display of form fields in the template
    fm = Registration(field_order=['email', 'city', 'first_name', 'last_name'])

    # Rendering the 'registration.html' template and passing the form object in context
    return render(req, 'student/registration.html', {'form': fm})


# View function to handle the login page
def login(req):
    # Different ways to customize form display (commented out for now):

    # Set custom ID format for each form field: id_<field_name>
    # fm = Login(auto_id='id_%s')

    # Use default auto-generated IDs
    # fm = Login(auto_id=True)

    # Disable automatic ID generation
    # fm = Login(auto_id=False)

    # Set a custom prefix for all IDs (all IDs would start with 'Rohan')
    # fm = Login(auto_id='Rohan')

    # Set a custom label suffix (adds a character like ':' or '-' after field labels)
    # fm = Login(label_suffix='A')  
    # fm = Login(label_suffix=' ')  # No suffix after labels

    # Set initial (pre-filled) value for the email field
    fm = Login(initial={'email': 'rohan@gmaail.com'})

    # Rendering the 'login.html' template and passing the form object in context
    return render(req, 'student/login.html', {'form': fm})
