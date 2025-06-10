from django import forms
from .models import Tasks
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm


class TaskForm(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = ['title', 'description', 'priority', 'status', 'file']
    

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username' , 'email' , 'password1' , 'password2']
