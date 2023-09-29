from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    avatar = models.ImageField()
    age = models.DateField()
    balance = models.PositiveIntegerField()

    def __str__(self):
        return f'Аккаунт пользователя {self.username}'

