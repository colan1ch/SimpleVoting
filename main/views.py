import datetime
from django.contrib.auth import login, logout
from django.http import Http404
from django.views.generic import CreateView
from .models import *
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from .forms import *
import json
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404


def get_menu_context():
    return [
        {'url_name': 'index', 'name': 'Главная'},
        {'url_name': 'time', 'name': 'Текущее время'},
    ]


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
        profile = Profile()
        profile.bio = ''
        profile.user = user
        profile.logo_image = None
        profile.save()
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


def logoutUser(request):
    logout(request)
    return redirect('index')


def profile_page(request):
    profile = Profile.objects.get(user=request.user)
    context = {
        'pagename': 'Профиль',
        'menu': get_menu_context(),
        'profile': profile,
        'can_change': True
    }
    return render(request, 'pages/profile.html', context)


def profile_page_id(request, id):
    profile = Profile.objects.get(user=User.objects.get(id=id))
    context = {
        'pagename': 'Профиль',
        'menu': get_menu_context(),
        'profile': profile,
        'can_change': request.user == profile.user
    }
    return render(request, 'pages/profile.html', context)


def votings_page(request):
    context = {
        'votings': Voting.objects.all()
    }
    return render(request, 'votings.html', context)


@login_required(login_url='/login/')
def create_voting_page(request):
    if request.method == 'POST':
        params = dict(request.POST)
        title = params['title'][0].strip()
        text = params['text'][0].strip()
        op = int(params['type'][0])
        options = json.dumps(params['options'])
        if check_param(title) and check_param(text) and check_list_param(params['options']) and check_type(op):
            voting = Voting(title=title, text=text, type=op, options=options, user=request.user)
            voting.save()
            messages.add_message(request, messages.SUCCESS, "Create successfully")
            return redirect(f'/voting/{voting.id}')
        else:
            messages.add_message(request, messages.ERROR, "Some errors")
    return render(request, 'create_voting.html')


def voting_page(request,id):
    voting = Voting.objects.get(id=id)
    vote = Vote.objects.filter(voting=voting)
    comments = Comment.objects.filter(voting=voting)
    options = json.loads(voting.options)
    content = {}
    for i in range(1,len(options)+1):
        if Vote.objects.filter(voting=voting).count() != 0:
            content[i]= int(Vote.objects.filter(voting=voting,option=i).count()/Vote.objects.filter(voting=voting).count()*100)
        else:
            content[i] = 0
    context = {
        'voting': voting,
        'options': options,
        'content': content,
        'comments': comments
        }
    return render(request, 'voting.html', context)

@login_required(login_url='/login/')
def add_comment(request,id):
    if request.method == 'POST' and len(request.POST)>1:
        if request.POST['comment'].strip()!='':
            voting = get_object_or_404(Voting, id=id)
            comment = Comment()
            comment.text = request.POST['comment'].strip()
            comment.user = request.user
            comment.voting = voting
            comment.save()
    return redirect(f'/voting/{id}')

@login_required(login_url='/login/')
def add_vote(request,id):
    if request.method == 'POST':
        voting = get_object_or_404(Voting, id=id)
        options = json.loads(voting.options)
        can_vote = not bool(Vote.objects.filter(voting=voting,user=request.user).count())
        if can_vote and len(request.POST) > 1:
            params = list(set(dict(request.POST)['option']))
            if voting.type == 1:
                params = params[:1]
            for i in params:
                if int(i) in list(range(1, len(options) + 1)):
                    vote = Vote(option=int(i), user=request.user, voting=voting)
                    vote.save()
    return redirect(f'/voting/{id}')
