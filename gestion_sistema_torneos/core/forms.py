from django import forms
from django.forms import ModelForm
from .models import Equipo
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class equipoForm(ModelForm):

    class Meta:
        model = Equipo
        fields = ['nombre', 'ciudad','maestro','imagen']


class CustomUserForm(UserCreationForm):
    class Meta:
        model=User
        fields =['first_name','last_name','email','username','password1','password2']