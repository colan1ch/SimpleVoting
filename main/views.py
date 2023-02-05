import datetime

from django.shortcuts import render


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

def edit_profile_page(request):
    context = {
        'pagename': 'Редактирование профиля',
        'menu': get_menu_context(),
        'oldpass': oldpass,
        'newpass': newpass,
        'email': email,
        'name': name,
        'surname': surname,
        'login': login
    }
    return render(request, 'pages/editprofile.html', context)
    def edit_voting_page(request, id):
    context = {  
        'menu': get_menu_context(),
        'oldpass': oldpass,
        'newpass': newpass,
        'email': email,
        'name': name,
        'surname': surname,
        'login': login
    }
    if request.method == 'POST':
         pass 
    return render(request, 'pages/editprofile.html', context)
  


