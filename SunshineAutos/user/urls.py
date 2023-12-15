from django.urls import path
from .views import *


urlpatterns = [
    path('logout/', LogoutView.as_view(), name='logout'),
    path('login/', LoginUserView.as_view(), name='login'),
    path('registration', register, name='registration')
]