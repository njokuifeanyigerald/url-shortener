from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model
from django import forms


class RegisterForm(UserCreationForm):
    email = forms.CharField(widget=forms.TextInput(attrs={
        "type": "email",
        "placeholder": "Email",
        'class' : "form-control me-2 text-center",
        'placeholder': 'enter an email address',
        'style': 'width: 300px; margin-left: 400px '
    }))
    username = forms.CharField(widget=forms.TextInput(attrs={
       "type": "text",
        "placeholder": "Username",
        'class' : "form-control me-2 text-center",
        'placeholder': 'enter a username',
        'style': 'width: 300px; margin-left: 400px '
    }))
    password1 = forms.CharField(widget=forms.TextInput(attrs={
        "type": "password",
        "placeholder": "Password",
        'class' : "form-control me-2 text-center",
        'placeholder': 'enter password',
        'style': 'width: 300px; margin-left: 400px '
    }))
    password2 =  forms.CharField(widget=forms.TextInput(attrs={
        "type": "password",
        "placeholder": "Confirm Password",
        'class' : "form-control me-2 text-center",
        'placeholder': 'confirm password',
        'style': 'width: 300px; margin-left: 400px '
    }))
    class Meta:
        model = get_user_model()
        fields = ('email', 'username', 'password1', 'password2')


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Email', widget=(forms.TextInput(attrs={
        "type": "email",
        "placeholder": "Email",
        'class' : "form-control me-2 text-center",
        'placeholder': 'enter your email',
        'style': 'width: 300px; margin-left: 400px '
    })))
    password = forms.CharField(label='Password', widget=(forms.TextInput(attrs={
        "type": "password",
        "placeholder": "Password",
        'class' : "form-control me-2 text-center",
        'placeholder': 'enter your password',
        'style': 'width: 300px; margin-left: 400px '
    })))
