from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.views import LoginView
from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from .forms import *

# Create your views here.

# Авторизация
class LoginUserView(LoginView):
    form_class = AccountLoginForm
    template_name = 'registration/login.html'
    redirect_authenticated_user = True

    def get_user_context(self, kwargs):
        context = kwargs

        return context

    def get_context_data(self, *, object_list=None, kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Авторизация")

        return dict(list(context.items()) + list(c_def.items()))


    def get_success_url(self):
        return reverse('main')


# Выход
class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login')


# Регситрация
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user =authenticate(username=form,password=password)
            login(request,user)
            return redirect('home')
        else:
            form = UserCreationForm()
    return render(request,'registration/register.html',{'form':form})



