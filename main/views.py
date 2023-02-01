import datetime
import sqlite3

from django.shortcuts import render

from models import Voting
from models import Vote
from forms import EditVotingForm


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

def edit_voting_page(request, id):
    context = { # получение данных для изменения из бд
        'title': Voting.title(id),  # заголовок
        'text': Voting.text(id),  # описание
        'type': Voting.type(id),  # тип голосования
        'options': Voting.options(id),  # (json) массив вариантов ответа
    }
    if request.method == 'POST': # если введены изменения
        arr = EditVotingForm(request.POST) # получение изменений
        if arr.is_valid():
            if arr.title:
                context['title'] = arr.title, # редактирование названия, уже имеющееся заголовок
            if arr.text:
                context['text'] = arr.text, # редактирование описания, уже имеющейся текст голосования
            if arr.type:
                context['type'] = arr.type, # редактирование типa голосования
            if arr.options:
                context['options'] = arr.options, # редактирование (json) массивa вариантов ответа
    else: # если изменения отсутствуют
        pass # ничего выполнять не требуется
    return render(request, 'pages/editvoting.html', context)
