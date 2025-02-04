from django.contrib.auth.forms import UserCreationForm
from .models import User
from django import forms
class CustomUserForm(UserCreationForm):
    username=forms.CharField(widget=forms.TextInput(attrs={'class':' use','placeholder':'Username'}))
    email=forms.CharField(widget=forms.TextInput(attrs={'class':' use','placeholder':'abcde@gmail.com'}))
    password1=forms.CharField(widget=forms.PasswordInput(attrs={'class':' use','placeholder':'Password'}))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={'class':' use','placeholder':'Confirm Password'}))
    class Meta:
        model=User
        fields=['username','email', 'password1','password2']