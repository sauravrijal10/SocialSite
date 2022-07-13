from asyncio import Task
from curses import use_env
from dataclasses import fields
from pyexpat import model
from re import template
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import UserRegistrationForm
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
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

# def register(request):
#     if request.method == 'POST':
#         user_form = UserRegistrationForm(request.POST)
#         if user_form.is_valid():
#             new_user = user_form.save(commit=False)
#             new_user.set_Password(
#                 user_form.cleaned_data['password']
#             )
#             new_user.save()
#             return render(request,'Site/register_done.html', {'new_user':new_user})
#         else:
#             user_form = UserRegistrationForm()
#         return render(request,'Site/register.html',{'user_form':user_form})

class RegisterPage(FormView):
    template_name = 'Site/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('home')

    def form_valid(self, form):
       user = form.save()
       if user is not None:
           login(self.request, user)
       return super(RegisterPage, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return  redirect('home')
        return super(RegisterPage, self).get(*args, **kwargs)





