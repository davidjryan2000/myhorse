from django import forms
from .models import Horse
from django.contrib.admin import widgets



class HorseForm(forms.ModelForm):
    class Meta:
        model = Horse
        fields = ['name', 'price', 'breed', 'location', 'age', 'sire', 'dam', 'image']


class LoginForm(forms.Form):
    username = forms.CharField(label='User Name', max_length=64)
    password = forms.CharField(widget=forms.PasswordInput())

    
