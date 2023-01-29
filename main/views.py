import datetime

from django.shortcuts import render
from main.models import Voting


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


def create_voting_page(request):
    if request.method == 'POST':
        f = Voting()
        f.title = request.POST["title"]
        f.text = request.POST["text"]
        f.type = request.POST["type"]
        f.options = request.POST["options"]
        f.user = request.user
        f.save()
    return render(request, 'create_voting.html', context={'page_css': 'create_voting.css'})
