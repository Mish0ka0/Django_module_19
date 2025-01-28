import random

from django.shortcuts import render
from django.http import HttpResponse
from task1.models import *

# Create your views here.


def start_menu(request):
    title = 'Игровой магазин'
    heading = 'Главная страница'
    context = {
        'title': title,
        'heading': heading
    }
    return render(request, 'start_menu.html', context)


def game_catalog(request):
    title = 'Каталог товаров'
    heading = 'Игры'
    games = Game.objects.all()
    button = 'Купить'
    back_button = 'Вернуться обратно'
    context = {
        'title': title,
        'heading': heading,
        'games': games,
        'button': button,
        'back_button': back_button
    }
    return render(request, 'game_catalog.html', context)


def shopping_cart(request):
    title = 'Корзина'
    heading = 'Корзина'
    text = 'Извините, ваша корзина пуста'
    back_button = 'Вернуться обратно'
    context = {
        'title': title,
        'heading': heading,
        'text': text,
        'back_button': back_button
    }
    return render(request, 'shopping_cart.html', context)


def sign_up_by_html(request):
    users = Buyer.objects.all()
    users_name = [user.name for user in users]
    info = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')
        info = {
            'username': username,
            'password': password,
            'repeat_password': repeat_password,
            'age': age
        }
        if password == repeat_password and username not in users_name and int(age) > 18:
            Buyer.objects.create(name=username, balance=random.randint(50, 2000), age=age)
            return HttpResponse(f'Приветсвуем, {username}!')
        if password != repeat_password:
            info.update({'error': "Пароли не совпадают"})
        if int(age) < 18:
            info.update({'error': "Вы должны быть старше 18"})
        if username in users:
            info.update({'error': "Пользователь уже существует"})

    return render(request, 'registration_page.html', info)
