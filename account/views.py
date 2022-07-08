from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from .forms import LoginForm, RegisterForm
from django.contrib.auth.models import User


def registerView(request):
    if request.user.is_authenticated:
        return redirect('blog:article_list')

    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('account:login')

    return render(request, 'account/register.html', context={'form': form})


def loginView(request):
    if request.user.is_authenticated:  # The logged in user does not have access to the login page
        return redirect('blog:article_list')

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = User.objects.get(username=form.cleaned_data.get('username'))
            login(request, user)
            return redirect('blog:article_list')
    else:
        form = LoginForm()
    return render(request, 'account/login.html', context={'form': form})


def logoutView(request):
    logout(request)
    return redirect('blog:article_list')
