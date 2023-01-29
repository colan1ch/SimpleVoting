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
    context = { # должны получать то, что есть
        'title': Voting.title,  # заголовок
        'text': Voting.text,  # описание
        'type': Voting.type,  # тип голосования
        'options': Voting.options,  # (json) массив вариантов ответа
    }
    if request.method == 'POST': # если введены изменения
        arr = EditVotingForm(request.POST) # получение изменений (не готово!!!)
        if arr.is_valid():
            context = {
                'title' : arr.title, # редактирование названия, уже имеющееся заголовок
                'text' : arr.text, # редактирование описания, уже имеющейся текст голосования
                'type': arr.type, #  редактирование типa голосования
                'options' : arr.options, #  редактирование (json) массивa вариантов ответа
            }
    #else: # если изменения отсутствуют
        #context['nothing_entered'] = True
        #context['form'] = EditVotingForm()
    return render(request, 'pages/editvoting.html', context)


#def create_voting_page(request):
#    context = {}
#    if request.method == 'post':
#        f = CreateVotingForm(request.POST)
#        if f.is_valid():
#            context = {
#                'title_form': f.title,
#                'text_form': f.text,
#                'type_form': f.type,
#                'option_1_form': f.option_1,
#                'option_2_form': f.option_2,
#                'option_3_form': f.option_3,
#                'option_4_form': f.option_4
#            }
#    else:
#
#        context['form'] = CreateVotingForm()
#
#    return render(request, 'pages/createvoting.html', context)

