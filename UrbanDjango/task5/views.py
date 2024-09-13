from collections import defaultdict
from django.shortcuts import render, HttpResponse
from .forms import UserRegister

# Create your views here.

def sign_up_by_django(request):
    users = ['Nikita', 'Denis', 'Mark']
    info = {}
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']
            if username not in users and age >= 18 and password == repeat_password:
                return HttpResponse(f'Приветствуем {username}!!')
            if password != repeat_password:
                info['error'] = 'Пароли не совпадают!'
                return render(request, 'fifth_task/registration_page.html', {'info': info})
            if age < 18:
                info['error'] = 'Вы должны быть старше 18'
                return render(request, 'fifth_task/registration_page.html', {'info': info})
            if username in users:
                info['error'] = 'Пользователь уже существует!'
                return render(request, 'fifth_task/registration_page.html', {'info': info})
    else:
        form = UserRegister()
    return render(request, 'fifth_task/registration_page.html', {'form': form})


def sign_up_by_html(request):
    users = ['Nikita', 'Denis', 'Mark']
    info = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')
        if username not in users and int(age) >= 18 and password == repeat_password:
            return HttpResponse(f'Приветствуем {username}!!')
        if password != repeat_password:
            info['error'] = 'Пароли не совпадают!'
            return render(request, 'fifth_task/registration_page.html', {'info': info})
        if int(age) < 18:
            info['error'] = 'Вы должны быть старше 18'
            return render(request, 'fifth_task/registration_page.html', {'info': info})
        if username in users:
            info['error'] = 'Пользователь уже существует!'
            return render(request, 'fifth_task/registration_page.html', {'info': info})
    return render(request, 'fifth_task/registration_page.html')


