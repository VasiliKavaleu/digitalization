from django.shortcuts import render, redirect
from . forms import SignUpForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def login_user(request):
    form = LoginForm()
    if request.method == 'POST':
        email = request.POST['email']
        print(email)
        password = request.POST['password']
        print(password)
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
            return render(request, 'login.html')
        else:
            return render(request, 'register.html', {'form': form})
    return render(request, 'register.html', {'form': form})
