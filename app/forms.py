from django import forms

class DataForm(forms.Form):
    url = forms.CharField(widget=forms.URLInput(attrs={
        'class' : "form-control ",
        'placeholder': 'enter a url link'
    }))
