from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = [
            'username', 'email', 'password1', 'password2'
        ]


class DataForm(forms.Form):
    url = forms.CharField(widget=forms.URLInput(attrs={
        'class' : "form-control me-2 text-center",
        'placeholder': 'enter a url link',
        'style': 'width: 300px '
    }))

