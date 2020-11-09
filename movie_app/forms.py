from django import forms
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class DateInput(forms.DateInput):
    input_type = 'date'
    
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required = False)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class MovieForm(forms.ModelForm):

    class Meta:
        model = Movie
        exclude = ['slug']
        widgets = {
            'year_of_release': DateInput()
        }