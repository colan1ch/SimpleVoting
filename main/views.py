import datetime

from django.shortcuts import render
from .models import *


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


def profile_page(request):
    user = Profile.user.objects.filter(id=request.user.id)
    context = {
        'pagename': 'Профиль',
        'menu': get_menu_context(),
        'user': user
    }
    return render(request, 'pages/profile.html', context)


def profile_page_id(request, id):
    user = Profile.user.objects.filter(id=request.user.id)
    context = {
        'pagename': 'Профиль',
        'menu': get_menu_context(),
        'user': user
    }
    return render(request, 'pages/profile.html', context)
