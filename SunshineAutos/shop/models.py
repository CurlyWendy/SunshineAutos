from django.db import models


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