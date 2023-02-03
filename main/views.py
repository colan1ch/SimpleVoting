import datetime

from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from main.forms import RegisterUserForm


def get_menu_context():
    return [
        {'url_name': 'index', 'name': 'Главная'},
        {'url_name': 'time', 'name': 'Текущее время'},
    ]


def index_page(request):
    context = {
        'pagename': 'Главная',
        'author': 'Andrew',
        'pages': 4,
        'menu': get_menu_context()
    }
    return render(request, 'pages/index.html', context)


def time_page(request):
    context = {
        'pagename': 'Текущее время',
        'time': datetime.datetime.now().time(),
        'menu': get_menu_context()
    }
    return render(request, 'pages/time.html', context)

class Registration(User):
    form_class = RegisterPage
    template_name = 'templates/register.html'
    
    def register_page(request):
        context = {
            'pagename': 'Регистрация',
            'login': 'Введите логин',
            'email' : 'Введите email',
            'first_name': 'Введите имя',
            'last_name': 'Введите фамилию',
            'password' : 'Введите пароль',
            'password_again': 'Повторите пароль',
        }
        return render(request, 'pages/register.html', context)
