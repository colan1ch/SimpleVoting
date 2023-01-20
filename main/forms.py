from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class LoginPage(AuthenticationForm):
    username = forms.CharField(label='Login', widget=forms.TextInput())
    password = forms.CharField(label='Password', widget=forms.PasswordInput())
