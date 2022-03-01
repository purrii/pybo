from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# 계정 생성시 사용할 USERFORM
class UserForm(UserCreationForm):
    email = forms.EmailField(label='이메일')

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'email')