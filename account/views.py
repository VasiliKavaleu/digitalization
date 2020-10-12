from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from . forms import SignUpForm, LoginForm, UpdateUserData
from .models import CustomUser, Industry


def login_user(request):
    form = LoginForm()
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('main')
        else:
            messages.info(request, 'Нет такого пользователя! Проверьте введенные данные.')
            return redirect('account:login_user')
    else:
        return render(request, 'login.html', {'form': form})


def logout_user(request):
    logout(request)
    return redirect('main')


def register(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            login_user = authenticate(request,
                                      email=request.POST['email'],
                                      password=request.POST['password1']
                                      )
            if login_user is not None:
                login(request, login_user)
            messages.success(request, 'Вы успешно зарегистрированы!')
            return redirect('account:register')
        else:
            return render(request, 'register.html', {'form': form})
    return render(request, 'register.html', {'form': form})


@login_required
def update_user(request):
    try:
        user = CustomUser.objects.get(id=request.user.id)
    except CustomUser.DoesNotExist:
        messages.error(request, 'Произошла ошибка!')
        return redirect('account:update_user')
    else:
        form = UpdateUserData(initial={
                                        'first_name': user.first_name,
                                        'last_name': user.last_name,
                                        'email': user.email,
                                        'organisation': user.organisation,
                                        'industry': user.industry,
                                        })
        if request.method == 'POST':
            user.first_name = request.POST.get("first_name")
            user.last_name = request.POST.get("last_name")
            user.email = request.POST.get("email")
            user.organisation = request.POST.get("organisation")
            user.industry = Industry.objects.get(id=request.POST.get("industry"))
            user.save()
            messages.success(request, 'Данные успешно изменены!')
            return redirect('account:update_user')
    return render(request, 'update.html', {'form': form})


@login_required
def del_user(request):
    try:
        user = CustomUser.objects.get(id=request.user.id)
    except CustomUser.DoesNotExist:
        messages.error(request, 'Произошла ошибка!')
    else:
        logout(request)
        user.delete()
        return redirect('main')