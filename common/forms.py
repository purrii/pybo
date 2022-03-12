from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.forms import PasswordChangeForm

# 계정 생성시 사용할 USERFORM
class UserForm(UserCreationForm):
    email = forms.EmailField(label='이메일')
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'email')

class CustomUserChangeForm(UserChangeForm):
    email = forms.EmailField(label='이메일')
    class Meta:
        model = User
        fields = ('username', 'email')


