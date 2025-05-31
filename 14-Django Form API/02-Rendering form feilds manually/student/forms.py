from django import forms


# Defining the Registration form
class Registration(forms.Form):
    # Input field for user's first name (text field)
    first_name = forms.CharField()

    # Input field for user's last name (text field)
    last_name = forms.CharField()

    # Input field for user's email address (text field — EmailField can be used for better validation)
    email = forms.CharField()

    # Input field for user's city (text field)
    city = forms.CharField()