from django.contrib.auth import views as auth_views
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .forms import LoginForm, RegisterForm
from django.shortcuts import redirect, render

# @login_required(login_url='login')


class LoginView(auth_views.LoginView):
    form_class = LoginForm
    template_name = 'accounts/login.html'
    

class RegisterView(generic.CreateView):
    form_class = RegisterForm
    template_name = 'app/register.html'
    success_url = reverse_lazy('login')

def logoutView(request):
    logout(request)
    return redirect('login')
