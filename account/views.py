from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from . forms import SignUpForm, LoginForm, UpdateUserData
from .models import CustomUser

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
            form.save()
            messages.success(request, 'Вы успешно зарегистрированы!')
            return render(request, 'register.html', {'form': form})
        else:
            return render(request, 'register.html', {'form': form})
    return render(request, 'register.html', {'form': form})

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
                                        'organisation': user.organisation
                                        })
        if request.method == 'POST':
            user.first_name = request.POST.get("first_name")
            user.last_name = request.POST.get("last_name")
            user.email = request.POST.get("email")
            user.organisation = request.POST.get("organisation")
            user.save()
            messages.success(request, 'Данные успешно изменены!')
            return redirect('account:update_user')
    return render(request, 'update.html', {'form': form})

def del_user(request):
    try:
        user = CustomUser.objects.get(id=request.user.id)
    except CustomUser.DoesNotExist:
        messages.error(request, 'Произошла ошибка!')
    else:
        logout(request)
        user.delete()
        return redirect('main')