from django.shortcuts import render_to_response, render
from django.http import HttpResponse


def home(request):
  # return render_to_response('templates/base.html')
  return render(request, 'static_page/home.html', {})

def about(request):
  return render(request, 'static_page/about.html')

def contact(request):
  return render(request, 'static_page/contact.html')

def sign_in(request):
  return render(request, 'static_page/registrations/sign_in.html')

def sign_up(request):
  return render(request, 'static_page/registrations/sign_up.html')

def profile(request):
  return render(request, 'static_page/registrations/profile.html')

def post_detial(request):
  return render(request, 'static_page/post_detial.html')

def forget_pwd(request):
  return render(request, 'static_page/registrations/forget_pwd.html')
