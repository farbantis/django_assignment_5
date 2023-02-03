from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods

from .forms import QuestionForm, UserLoginForm, UserRegisterForm, ChangePasswordForm
from .models import TaskUser, Note


def index(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            print('is valid form')
            return redirect('task_5:accept')
        else:
            return redirect('task_5:deny')
    else:
        form = QuestionForm()
    context = {'form': form}
    return render(request, './index.html', context)


def accept(request):
    return render(request, './accept.html')


def deny(request):
    return render(request, './deny.html')


def login_user(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['login'], password=cd['password'])
            if user is not None:
                login(request, user)
                return redirect('task_5:home')
    form = UserLoginForm()
    return render(request, './login.html', {'form': form})


def logout_user(request):
    logout(request)
    return redirect('task_5:index')


def register_user(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            new_user = TaskUser(username=cd['username'])
            new_user.save(commit=False)
            new_user.set_password(cd['password'])
            new_user.save()
    else:
        form = UserRegisterForm()
    return render(request, './register.html', {'form': form})


@login_required
def change_password(request):
    if request.method == 'POST':
        form = ChangePasswordForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            if request.user.check_password(cd['current_password']):
                user = TaskUser.objects.get(username=request.user)
                user.set_password(cd['password'])
                user.save()
                return redirect('task_5:index')
    form = ChangePasswordForm()
    return render(request, './change_password.html', {'form': form})


@login_required
@require_http_methods(["GET"])
def home(request):
    note = request.GET.get('note')
    author = request.GET.get('check')
    if note and author:
        notes = Note.objects.filter(text__icontains=note).filter(author__username=request.user)
    elif note:
        notes = Note.objects.filter(text__icontains=note)
    elif author:
        notes = Note.objects.filter(author__username=request.user)
    else:
        notes = Note.objects.all()
    context = {'notes': notes}
    return render(request, './home_page.html', context)
