from django import forms

class LoginForm(forms.form):
    username = forms.CharField
    password = forms.CharField(widget=forms.PasswordInput)