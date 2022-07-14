from re import template
from django.urls import URLPattern, path, include
from . import views
from django.contrib.auth.views import LogoutView

from .views import UserLogin , Homepage, RegisterPage

urlpatterns = [
    path('', views.UserLogin.as_view(),name='login'),
    path('home', views.Homepage, name = 'home'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', views.RegisterPage.as_view(), name='register'),
    # path('login', views.tasklist, name = 'homepage'),
]
