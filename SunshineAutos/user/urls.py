from django.urls import path
from .views import *


urlpatterns = [
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signin/', LoginUserView.as_view(), name='signin'),
    path('singup', register, name='singup')
]