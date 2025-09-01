from django.forms import ModelForm
from .models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Address
from django import forms
class RegisterForm(UserCreationForm):

    class Meta:
        fields = ['username','email','user_type']    
        model = User

class LoginForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(max_length=30,widget=forms.PasswordInput)
class AddressForm(ModelForm):
    class Meta:
        model = Address
        exclude = ["user"]