from django.shortcuts import render
from django.contrib.auth import login
from django.contrib.auth import views


class LoginView(views.LoginView):
    template_name = 'users/login.html'
    