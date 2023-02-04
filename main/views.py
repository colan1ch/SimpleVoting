import datetime

from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from .forms import *

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

class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'registration/registration.html'
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = {
            'form': self.get_form(),
        }
        return context

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('index')

class LoginUser(LoginView):
    form_class = LoginPage
    template_name = 'registration/login.html'

    def get_context_data(self, **kwargs):
        context = {
            'form': self.get_form(),
        }
        return context

    def get_success_url(self):
        return reverse_lazy('index')

