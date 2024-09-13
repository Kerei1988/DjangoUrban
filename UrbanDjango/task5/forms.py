from django import forms
from django.forms import PasswordInput


class UserRegister(forms.Form):
    username = forms.CharField(max_length=30, label='Введите логин:')
    password = forms.CharField(widget=PasswordInput, min_length=8, label='Введите пароль:')
    repeat_password = forms.CharField(widget=PasswordInput, min_length=8, label='Повторите пароль:')
    age = forms.IntegerField(max_value=100, label='Введите свой возраст:')
