from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from .models import User


class AccountRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class AccountLoginForm(AuthenticationForm):
    username = forms.CharField(label='Логин', )
    password = forms.CharField(label='Пароль', )