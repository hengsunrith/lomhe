from django.urls import path

from . import views

# app_name = 'static_page'
urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('sign_in/', views.LoginView.as_view(), name='sign_in'),
    path('sign_up/', views.RegisterView.as_view(), name='sign_up'),
    path('logout/', views.logout_view, name='logout'),
    path('forget_pwd/', views.ForgetPwdView.as_view(), name='forget_pwd'),
    path('profile/', views.profile, name='profile'),
    path('post_detial/', views.post_detial, name='post_detial'),
]
