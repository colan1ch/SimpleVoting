import datetime

from django.shortcuts import render

from models import Voting
from models import Vote


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
    context = {
        'title' : Voting.title, # редактирование названия, уже имеющееся заголовок
        'text' : Voting.text, # редактирование описания, уже имеющейся текст голосования
        'type': Voting.type, # тип голосования
        'options' : Voting.options, # json массив вариантов ответа
        'user_make' : Voting.user, # индекс пользователя, создавшего голосование(как я понял)

        # далее при многовыборочном голосовании создаётся несколько штук
        'options' : Vote.option, # индекс ответа в json массиве
        'user_voting' : Vote.user, # индекс проголосовавшего пользователя (как я понял)
        'voting' : Vote.voting # models.ForeignKey(to=Voting, on_delete=models.CASCADE)
    }
    return render(request, 'editvoting/' + str(id), context)

