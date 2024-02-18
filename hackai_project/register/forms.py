from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import models

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2','groups']
        widgets = {
            'myfield': forms.TextInput(attrs={'class': 'myfieldclass'}),
        }

class LoginForm(forms.Form):
    TYPE_CHOICES = (
    ("S", "Students"),
    ("F", "Faculty"),
    ("St", "Staff"),

)

    group = forms.ChoiceField(choices= TYPE_CHOICES)
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

