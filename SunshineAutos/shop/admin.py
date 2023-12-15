from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(CarType)
admin.site.register(CarColor)
admin.site.register(CarMake)
admin.site.register(Car)
admin.site.register(Basket)
admin.site.register(OrderItem)
admin.site.register(Order)