from asyncio import Task
from dataclasses import fields
from pyexpat import model
from re import template
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
# from .forms import LoginForm
# from requests import request
# from requests import request

# def user_login(request):


class UserLogin(LoginView):
    template_name = 'Site/login.html'
    fields = '__all__'
    redirect_authenticated_user = True


    def get_success_url(self):
        return reverse_lazy('home')

    # def login(self, request):
    #     form = 'helo saurav'
    #     return render(request, 'Site/login.html', context=form)

def tasklist(request):
    return render(request, 'Site/login.html')

def Homepage(request):
    return render (request, 'Site/home.html')
    template_name = 'Site/home.html'
    context_object_name = 'home'

# class Homepage(LoginRequiredMixin):
#     context_object_name='home'
#     model='task'
    
    

# def homepage(request):
#     return render(request, 'home.html')
# class Login(LoginView):
#     template_name = 'login.html'
#     fields = '__all__'
#     redirect_authenticated_user = True

#     def get_success_url(self):
#         return reverse_lazy('newsfeed')

# class Newsfeed(LoginRequiredMixin):
#     template_name = 'templates/login.html'

#     context_object__name = 'newsfeed'




