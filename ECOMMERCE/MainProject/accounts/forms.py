from django.forms import ModelForm
from .models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Address
from django import forms
class RegisterForm(UserCreationForm):

    class Meta:
        fields = ['username','email','user_type','gender']    
        model = User
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user_type'].choices = [
                (value, label) for value, label in self.fields['user_type'].choices
                if value != 'Admin'
            ]
    def clean_user_type(self):
        user_type = self.cleaned_data.get('user_type')
        if user_type == "Admin":
            raise forms.ValidationError("You cannot register as Admin.")
        return user_type
class LoginForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(max_length=30,widget=forms.PasswordInput)
class AddressForm(ModelForm):
    class Meta:
        model = Address
        exclude = ["user"]
from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class edit_profile_form(forms.ModelForm):
    class Meta:
        model = User   # 👈 this was missing
        fields = ['username', 'email', 'gender', 'user_type']  
        # include only fields you want the user to edit
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user_type'].choices = [
                (value, label) for value, label in self.fields['user_type'].choices
                if value != 'Admin'
            ]

