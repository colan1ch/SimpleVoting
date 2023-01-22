from django import forms

class RegisterForm(forms.Form):
    login = forms.CharField(label='Your login')
    first_name = forms.CharField(label='Your first_name')
    last_name = forms.CharField(label='Your last_name')
    email = forms.CharField(label='Your email')
    password = forms.CharField(label='Your password')
    password_again = forms.CharField(label='Your password again')

