from django.db import models
from user.models import User


class CarType(models.Model):
    name = models.CharField(max_length = 20, unique = True)

    def __str__(self):
        return f'Тип автомобиля {self.name}'


class CarColor(models.Model):
    name = models.CharField(max_length = 20, unique = True)

    def __str__(self):
        return f'Цвет машины {self.name}'


class CarMake(models.Model):
    name = models.CharField(max_length = 40, unique = True)

    def __str__(self):
        return f'Марка автомобиля {self.name}'


class Car(models.Model):
    car_make = models.ForeignKey(
        CarMake,
        on_delete = models.CASCADE,
        related_name = 'carmake'
    )
    car_model = models.CharField(max_length = 40)
    car_price = models.PositiveIntegerField()
    car_picture = models.ImageField()
    car_type = models.ForeignKey(
        CarType,
        on_delete = models.CASCADE,
        related_name = 'cartype'
    )
    car_color = models.ForeignKey(
        CarColor,
        related_name = 'carcolor',
        on_delete=models.CASCADE
    )
    in_stock = models.BooleanField(default = True)
    year_manufacture = models.DateField()

    def __str__(self):
        return f'Автомобиль {self.car_make} {self.car_model} {self.car_color} цвета'


class Basket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Car, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    created_timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'

    def __str__(self):
        return f'Корзина для {self.user.username} | Товар {self.product.name}'

    def sum(self):
        return self.quantity * self.product.price


class OrderItem(models.Model):
    product = models.ForeignKey(Car, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    price = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = 'Заказанный товар'
        verbose_name_plural = 'Заказанные товары'


    def total_price(self):
        return self.quantity * self.price

    def __str__(self):
        return f'Товар заказан {self.product.name}'


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    created_timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


    def total_price(self):
        return sum(item.total_price() for item in self.items.all())

    def __str__(self):
        return f'Заказ пользователя {self.user.username} '