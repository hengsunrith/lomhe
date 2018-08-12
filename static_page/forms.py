from django import forms
from django.contrib.auth.models import User


class LoginUserForm(forms.ModelForm):
  username = forms.CharField(widget=forms.TextInput)
  password = forms.CharField(widget=forms.PasswordInput)

  class Meta:
    model = User
    fields = ['username', 'password']


class RegisterUserForm(forms.ModelForm):
  username = forms.CharField(widget=forms.TextInput)
  email = forms.CharField(widget=forms.EmailInput)
  password = forms.CharField(widget=forms.PasswordInput)
  confirm_password = forms.CharField(widget=forms.PasswordInput)

  class Meta:
    model = User
    fields = ['username', 'email', 'password']


class ForgetPwdForm(forms.ModelForm):
  old_password = forms.CharField(widget=forms.PasswordInput)
  password = forms.CharField(widget=forms.PasswordInput)
  confirm_password = forms.CharField(widget=forms.PasswordInput)

  class Meta:
    model = User
    fields = ['password']
