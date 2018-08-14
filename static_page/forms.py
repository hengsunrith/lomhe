from django import forms
from django.contrib.auth.models import User


class LoginUserForm(forms.ModelForm):
  username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
  password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

  class Meta:
    model = User
    fields = ['username', 'password']


class RegisterUserForm(forms.ModelForm):
  username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
  email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
  password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
  confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

  class Meta:
    model = User
    fields = ['username', 'email', 'password']


class ForgetPwdForm(forms.ModelForm):
  password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
  confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

  class Meta:
    model = User
    fields = ['password']


class PostForm(forms.ModelForm):
  body = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
  file = forms.FileField(widget=forms.FileInput(attrs={'class': 'form-control'}))

