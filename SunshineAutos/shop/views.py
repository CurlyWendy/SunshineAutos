from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, View
from django.shortcuts import get_object_or_404, HttpResponseRedirect, redirect
from django.db.models import Q
from django.core.paginator import Paginator, Page

from .models import *


class MainPageListView(ListView):
    template_name = 'shop/index.html'

    def get(self, request, *args, **kwargs):
        context = {
            'products': Car.objects.filter(is_retro=True)
        }
        return render(request, self.template_name, context)


class ProductListView(ListView):
    template_name = 'shop/catalog.html'

    def get_queryset(self):
        queryset = Car.objects.all()

        product_types = self.request.GET.getlist('car_type')
        colors = self.request.GET.getlist('car_color')
        brands = self.request.GET.getlist('car_make')

        if product_types:
            product_type_filters = Q()
            for product_type in product_types:
                product_type_filters |= Q(car_type=product_type)
            queryset = queryset.filter(product_type_filters)

        if colors:
            colors_filters = Q()
            for color in colors:
                colors_filters |= Q(car_color=color)
            queryset = queryset.filter(colors_filters)

        if brands:
            brand_filters = Q()
            for brand in brands:
                brand_filters |= Q(car_make=brand)
            queryset = queryset.filter(brand_filters)

        return queryset

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        car_types = CarType.objects.values()
        brands = CarMake.objects.values()
        colors = CarColor.objects.values()
        page_number = request.GET.get('page')
        paginator = Paginator(queryset, 8)  # 10 товаров на странице
        page = paginator.get_page(page_number)

        return render(request,
                      self.template_name,
                      {'products': page,
                       'product_types': car_types,
                       'brands': brands,
                       'colors': colors,

                       }
                      )


class PremiumListView(ListView):
    template_name = 'shop/catalog.html'

    def get_queryset(self):
        queryset = Car.objects.filter(is_retro=True)

        product_types = self.request.GET.getlist('product_type')
        colors = self.request.GET.getlist('color')
        brands = self.request.GET.getlist('brand')

        if product_types:
            product_type_filters = Q()
            for product_type in product_types:
                product_type_filters |= Q(product_type=product_type)
            queryset = queryset.filter(product_type_filters)

        if colors:
            colors_filters = Q()
            for color in colors:
                colors_filters |= Q(color=color)
            queryset = queryset.filter(colors_filters)

        if brands:
            brand_filters = Q()
            for brand in brands:
                brand_filters |= Q(brand=brand)
            queryset = queryset.filter(brand_filters)

        return queryset

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()

        car_types = CarType.objects.values()
        brands = CarMake.objects.values()
        colors = CarColor.objects.values()
        page_number = request.GET.get('page')
        paginator = Paginator(queryset, 8)  # 10 товаров на странице
        page = paginator.get_page(page_number)

        return render(request,
                      self.template_name,
                      {'products': page,
                       'product_types': car_types,
                       'brands': brands,
                       'colors': colors,

                       }
                      )


class ProductView(View):
    queryset = Car.objects.all()
    template_name = 'shop/product.html'

    def get_object(self):
        id = self.kwargs.get('id')
        return get_object_or_404(self.queryset, id=id)

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        context = {'product': instance}

        return render(request, self.template_name, context)


class SearchListView(ListView):
    """
    Поиск
    """

    template_name = 'shop/search.html'

    def get_queryset(self):
        return Car.objects.filter(name__icontains=self.request.GET.get('q'))

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['q'] = self.request.GET.get('q')
        return context


class BasketListView(ListView):
    """
    Товары в корзине
    """
    template_name = 'shop/basket.html'

    def get_queryset(self):
        return Basket.objects.filter(user=self.request.user)

    def get_total_quantity(self):
        baskets = self.get_queryset()
        return sum(basket.quantity for basket in baskets)

    def get_total_sum(self):
        baskets = self.get_queryset()
        return sum(basket.sum() for basket in baskets)

    def get(self, request, *args, **kwargs):
        context = {
            'object_list': self.get_queryset(),
            'total_quantity': self.get_total_quantity(),
            'total_sum': self.get_total_sum(),
            'info_text': 'Ваша корзина пуста',
        }
        return render(request, self.template_name, context)


def basket_add(request, product_id):
    """
    Добавление товара в корзину
    """
    current_page = request.META.get('HTTP_REFERER')
    product = Car.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, product=product)

    if not baskets.exists():
        Basket.objects.create(user=request.user, product=product, quantity=1)
        return HttpResponseRedirect(current_page)
    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()
        return HttpResponseRedirect(current_page)


def basket_delete(request, id):
    """
    Удалить товар из корзины
    """
    basket = Basket.objects.get(id=id)
    basket.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def create_order(request):
    """
    Создать заказ
    """
    user = request.user

    basket_items = Basket.objects.filter(user=user)

    if basket_items.exists():
        order = Order.objects.create(user=user)

        for basket_item in basket_items:
            order_item = OrderItem.objects.create(
                product=basket_item.product,
                quantity=basket_item.quantity,
                price=basket_item.product.price * basket_item.quantity
            )
            order.items.add(order_item)

        basket_items.delete()

        return redirect('main')

class AboutUs(ListView):
    template_name = 'shop/about_us.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)