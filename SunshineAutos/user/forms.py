from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User


class AccountLoginForm(AuthenticationForm):
    username = forms.Charfield(label="Логин")
    password = forms.Charfield(label="Пароль")