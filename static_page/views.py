from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views import generic
from django.contrib.auth import authenticate, login, logout
from static_page.forms import RegisterUserForm, LoginUserForm, ForgetPwdForm
from django.contrib import messages

def home(request):
  return render(request, 'static_page/home.html', {})

def about(request):
  return render(request, 'static_page/about.html')

def contact(request):
  return render(request, 'static_page/contact.html')

def logout_view(request):
    logout(request)
    return redirect('/')


class LoginView(generic.CreateView):
  form_class = LoginUserForm
  template_name = 'static_page/registrations/sign_in.html'

  def get(self, request):
    form = self.form_class(None)
    return render(request, self.template_name, {'form': form})

  def dispatch(self, *args, **kwargs):
    if self.request.user.is_authenticated:
      return redirect('/')
    return super().dispatch(*args, **kwargs)

  def post(self, request):
    if request.method == 'POST':
      form = LoginUserForm(request.POST)
      if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        try:
          user = User.objects.get(username=username)
          if user.check_password(password):
            username = user.username
            user = authenticate(request, username=username, password=password)
            login(request, user)
            messages.success(request, "Welcome")
            return redirect('/')
          else:
            messages.error(request, "Password not match")
            return redirect('/sign_in/')
        except User.DoesNotExist:
          redirect('/sign_up/')
    else:
      form = LoginUserForm()
    return render(request, 'static_page/registrations/sign_in.html', {'form': form})


class RegisterView(generic.CreateView):
  form_class = RegisterUserForm
  template_name = 'static_page/registrations/sign_up.html'

  def get(self, request):
    form = self.form_class(None)
    return render(request, self.template_name, {'form': form})

  def post(self, request):
      if request.method == 'POST':
          form = RegisterUserForm(request.POST)
          if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/')
      else:
          form = RegisterUserForm()
      return render(request, 'static_page/registrations/sign_up.html', {'form': form})

  def dispatch(self, *args, **kwargs):
    if self.request.user.is_authenticated:
      return redirect('/')
    return super().dispatch(*args, **kwargs)


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
