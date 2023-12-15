from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    avatar = models.ImageField(null=True)
    age = models.DateField(null=True)
    balance = models.PositiveIntegerField(null=True)

    def __str__(self):
        return f'Аккаунт пользователя {self.username}'

