from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from .forms import AccountForm, LoginForm, NewpwForm
from .models import Account


# Create your views here.
def index(request):
    accounts = Account.objects.all()

    context = {
        'accounts': accounts
    }
    return render(request, 'login/index.html', context)

def signup(request):
    if request.method == 'POST':
        form = AccountForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            count = User.objects.filter(username=name).count()
            if count > 0:
                form.add_error('name', '이미 존재하는 이름입니다.')
                return render(request, 'login/signup.html', {'form' : form})

            pw = form.cleaned_data['pw']

            account = form.save(commit=False)
            user = User()
            user.username = account.name
            user.set_password(pw)
            user.save()
            account.user = user
            account.save()

            return redirect('index')
    else:
        form = AccountForm()

    return render(request, 'login/signup.html', {'form' : form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            pw = form.cleaned_data['pw']

            user = authenticate(request, username=username, password=pw)
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                form.add_error('pw', '로그인 정보가 올바르지 않습니다')
    else:
        form = LoginForm()

    return render(request, 'login/login.html',{'form':form})


def logout_view(request):
    logout(request)
    return redirect('index')


@login_required
def new_pw(request):
    if request.method == 'POST':
        form = NewpwForm(request.POST)

        if form.is_valid():
            current_pw = form.cleaned_data['current_pw']
            new_pw1 = form.cleaned_data['new_pw1']
            new_pw2 = form.cleaned_data['new_pw2']

            if not request.user.check_password(current_pw):
                form.add_error('current_pw', '현재 비밀번호가 일치하지 않습니다.')
                return render(request, 'login/new_pw.html',{'form':form})

            if new_pw1 != new_pw2:
                form.add_error('new_pw1', '비밀번호가 일치하지 않습니다.')
            else:
                request.user.set_password(new_pw2)
                request.user.save()
                login(request, request.user)
                return redirect('index')
    else:
        form = NewpwForm()
    return render(request, 'login/new_pw.html', {'form':form})

