import datetime
import json

from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from main.models import Voting, Vote
from main.forms import EditVotingForm

def check_type(op):
    if op == 1 or op == 2:
        return True
    else:
        return False


def check_list_param(param):
    if len(param) < 2:
        return False
    for i in param:
        print(i)
        if not check_param(i):
            return False
    return True


def check_param(param):
    blacklist = ['{', '}', '[', ']']
    param = param.split()
    param = ''.join(param)
    if len(param) == 0:
        return False
    for i in blacklist:
        if i in param:
            return False
    return True


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

@login_required()
def edit_voting_page(request, id):
    voting = voting = get_object_or_404(Voting, id=id)
    context = {}
    if request.user == voting.user:
        if request.method == 'POST':
            params = dict(request.POST)
            title = params['title'][0].strip()
            text = params['text'][0].strip()
            op = int(params['type'][0])
            options = json.dumps(params['options'])
            if check_param(title) and check_param(text) and check_list_param(params['options']) and check_type(op):
                voting = Voting(title=title, text=text, type=op, options=options, user=request.user)
                voting.save()
                messages.add_message(request, messages.SUCCESS, 'Editing success')
            else:
                messages.add_message(request, messages.ERROR, 'Editing error')
            return redirect(f'voting/{voting.id}')

        else:
            context['voting'] = voting
            return render(request, 'pages/editvoting.html', context)
    else:
        raise PermissionDenied()
