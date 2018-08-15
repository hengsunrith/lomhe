from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class LoginUserForm(forms.Form):
  username = forms.CharField(label='User Name:', widget=forms.TextInput(attrs={'class': 'form-control'}))
  password = forms.CharField(label='Password:', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
  remember_me = forms.BooleanField(label='Remember me:', required=False, widget=forms.CheckboxInput)

  class Meta:
    model = User
    fields = ['username', 'password']

class RegisterUserForm(forms.ModelForm):
  username = forms.CharField(label='User Name:', widget=forms.TextInput(attrs={'class': 'form-control'}))
  email = forms.EmailField(label='Email Address:',  widget=forms.EmailInput(attrs={'class': 'form-control'}))
  password = forms.CharField(label='Password:',  widget=forms.PasswordInput(attrs={'class': 'form-control'}))
  password2 = forms.CharField(label='Confirm Password:', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

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

