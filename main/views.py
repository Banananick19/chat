from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User, AnonymousUser
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .forms import *


# Create your views here.


def index(request):
    if not request.user or request.user.is_anonymous:
        return redirect(reverse_lazy('sing_in'))
    return render(request, 'main/index.html', {})


def lobby(request, lobby):
    if not request.user or request.user.is_anonymous:
        return redirect(reverse_lazy('sing_in'))
    return render(request, 'main/lobby.html', {'lobby': lobby})

def sing_up(request):
    if not request.user or not request.user.is_anonymous:
        return redirect(reverse_lazy('sing_in'))
    else:
        if request.method == 'POST':
            form = SingUpForm(request.POST)
            if form.is_valid():
                user = form.save()
                login(request, user)
                return redirect(reverse_lazy('index'))
            else:
                context = {
                    'form': form
                }
                return render(request, 'main/register_user.html', context)
        if request.method == 'GET':
            context = {
                'form': SingUpForm()
            }
            return render(request, 'main/register_user.html', context)

def sing_in(request):
    if request.method == 'POST':
        form = SingInForm(request.POST)
        if form.is_valid():
            if not request.user or request.user.is_anonymous:
                logout(request)
            try:
                user = User.objects.get(username=form.cleaned_data['username'])
            except:
                context = {
                    'form': form
                }
                return render(request, 'main/login.html', context)
            login(request, user)
            return redirect(reverse_lazy('index'))


        else:
            context = {
                'form': form
            }
            return render(request, 'main/login.html', context)
    if request.method == 'GET':
        context = {
            'form': SingInForm()
        }
        return render(request, 'main/login.html', context)




