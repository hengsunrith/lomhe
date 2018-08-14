from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class LoginUserForm(forms.ModelForm):
  username = forms.CharField(label=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'username'}))
  password = forms.CharField(label=False, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'password'}))
  remember_me = forms.BooleanField(required=False, widget=forms.CheckboxInput)

  class Meta:
    model = User
    fields = ['username', 'password']


class RegisterUserForm(forms.ModelForm):
  username = forms.CharField(label=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'username'}))
  email = forms.CharField(label=False,  widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'email'}))
  password = forms.CharField(label=False,  widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'password'}))
  password2 = forms.CharField(label=False, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'comfirm password'}))

  class Meta:
    model = User
    fields = ['username', 'email', 'password']

  # validate password
  def clean_password2(self):
    cd = self.cleaned_data
    if cd['password2'] != cd['password']:
      raise ValidationError("Password don't match!")
    return cd['password2']


class ForgetPwdForm(forms.ModelForm):
  password = forms.CharField(label=False, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'password'}))
  confirm_password = forms.CharField(label=False, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'confirm password'}))

  class Meta:
    model = User
    fields = ['password']


class PostForm(forms.ModelForm):
  body = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
  file = forms.FileField(widget=forms.FileInput(attrs={'class': 'form-control'}))

