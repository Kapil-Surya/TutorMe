#import email
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class LoginForm(forms.Form):
    username = forms.CharField(max_length=200)
    password = forms.CharField(widget = forms.PasswordInput)

class RegisterForm(UserCreationForm):
    username = forms.CharField(required=True,max_length=200)
    email = forms.EmailField(required=True)
    password1 = forms.CharField(min_length=8,required=True,widget=forms.PasswordInput)
    password2 = forms.CharField(min_length=8,required=True,widget=forms.PasswordInput)
    #username = forms.CharField(max_length=200)
    #email = forms.EmailField()
    class Meta:
              model = User
              fields = ("username","email","password1","password2")
              
		
    

    #class Meta:
     #   model = User
      #  fields = ["username", "email", "password1", "password2"]

