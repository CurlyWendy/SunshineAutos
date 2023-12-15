from django.urls import path
from .views import *


urlpatterns = [
    path('', MainPageListView.as_view(), name='main'),
    path('product/<int:id>/', ProductView.as_view(), name='product-detail'),
    path('catalog/', ProductListView.as_view(), name='catalog'),
    path('premium/', PremiumListView.as_view(), name='premium'),
    path('basket/', BasketListView.as_view(), name='basket'),
    path('basket-add/<int:product_id>/', basket_add, name='basket_add'),
    path('basket-delete/<int:id>/', basket_delete, name='basket_delete'),
    path('search', SearchListView.as_view(), name='search'),
    path('create-order', create_order, name='create_order'),
    path('about_us', AboutUs.as_view(), name='about_us'),
]