from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django_auth_goblin.forms import LoginForm, RegisterForm
from django.contrib.auth.models import User

# Create your views here.
def login_register_view(request):
    login_form = LoginForm(data=request.POST or None)
    register_form = RegisterForm(data=request.POST or None)

    if 'login_submit' in request.POST and login_form.is_valid():
        user = login_form.get_user()
        login(request, user)
        return redirect(reverse('next-page'))

    if 'register_submit' in request.POST and register_form.is_valid():
        user = register_form.save()
        login(request, user)
        return redirect(reverse('next-page'))

    return render(request, 'django_auth_goblin/login_register.html', {
        'login_form': login_form,
        'register_form': register_form,
    })

def next_page_view(request):
    return render(request, 'django_auth_goblin/next_page.html')

