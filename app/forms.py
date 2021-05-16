from django import forms

class DataForm(forms.Form):
    url = forms.CharField(widget=forms.URLInput(attrs={
        'class' : "form-control me-2 text-center",
        'placeholder': 'enter a url link',
        'style': 'width: 300px '
    }))
