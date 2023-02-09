import datetime
import sqlite3

from django.shortcuts import render

from main.models import Voting, Vote
from main.forms import EditVotingForm


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

    conn = sqlite3.connect("0001.db") # подключение бд
    curs = conn.cursor()

    curs.execute("SELECT * FROM Voting WHERE id = ?", (id, )) # достаём ин-фу из бд
    from_bd = curs.fetchone(id)

    tmp_title = from_bd['title'] # ин-фу из бд записываем в переменные
    tmp_text = from_bd['text']
    tmp_type = from_bd['type']
    tmp_options = from_bd['options']
    tmp_user = from_bd['user']

    if request.method == 'POST':  # если введены изменения
        arr = EditVotingForm(request.POST)  # получение изменений
        if arr.is_valid():
            if arr['title']:
                sql = """UPDATE Voting SET title = %s WHERE id = %s"""
                curs.execute(sql, (arr['title'], id))
                tmp_title = arr.title,  # редактирование названия
            if arr['text']:
                sql = """UPDATE Voting SET text = %s WHERE id = %s"""
                curs.execute(sql, (arr['text'], id))
                tmp_text = arr['text'],  # редактирование описания
            if arr['type']:
                sql = """UPDATE Voting SET type = %s WHERE id = %s"""
                curs.execute(sql, (arr['type'], id))
                tmp_type = arr['type'],  # редактирование типa голосования
            if arr['options']:
                sql = """UPDATE Voting SET options = %s WHERE id = %s"""
                curs.execute(sql, (arr['options'], id))
                tmp_options = arr['options'],  # редактирование (json) массивa вариантов ответа

    else:  # если изменения отсутствуют
        pass  # ничего выполнять не требуется

    conn.close() # прекращаем работу с бд

    context = {
        'title': tmp_title,  # заголовок
        'text': tmp_text,  # описание
        'type': tmp_type,  # тип голосования
        'options': tmp_options,  # (json) массив вариантов ответа
        'user' : tmp_user,
    }

    return render(request, 'pages/editvoting.html', context)
