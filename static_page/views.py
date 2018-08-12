from django.shortcuts import render_to_response, render
from django.http import HttpResponse
from django.views import generic
from static_page.forms import RegisterUserForm, LoginUserForm, ForgetPwdForm


def home(request):
  # return render_to_response('templates/base.html')
  return render(request, 'static_page/home.html', {})

def about(request):
  return render(request, 'static_page/about.html')

def contact(request):
  return render(request, 'static_page/contact.html')

# def sign_in(request):
#   return render(request, 'static_page/registrations/sign_in.html')
class LoginView(generic.CreateView):
  form_class = LoginUserForm
  template_name = 'static_page/registrations/sign_in.html'

  def get(self, request):
    form = self.form_class(None)
    return render(request, self.template_name, {'form': form})

# def sign_up(request):
#   return render(request, 'static_page/registrations/sign_up.html')
class RegisterView(generic.CreateView):
  form_class = RegisterUserForm
  template_name = 'static_page/registrations/sign_up.html'

  def get(self, request):
    form = self.form_class(None)
    return render(request, self.template_name, {'form': form})


# def forget_pwd(request):
  # return render(request, 'static_page/registrations/forget_pwd.html')
class ForgetPwdView(generic.CreateView):
  form_class = ForgetPwdForm
  template_name = 'static_page/registrations/forget_pwd.html'

  def get(self, request):
    form = self.form_class(None)
    return render(request, self.template_name, {'form': form})


def profile(request):
  return render(request, 'static_page/registrations/profile.html')

def post_detial(request):
  return render(request, 'static_page/post_detial.html')
