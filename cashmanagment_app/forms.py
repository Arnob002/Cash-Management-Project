from django import forms
from cashmanagment_app.models import *
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm

class RegisterForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = ['username','email','password1','password2']

class LoginForm(AuthenticationForm):
   pass 

class AddCashForm(forms.ModelForm):
    class Meta:
        model = AddCashModel
        fields = '__all__'
        exclude = ['user']

        widgets = {
            'datetime': forms.DateTimeInput(attrs= {'type':'datetime-local'})
            }

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = ExpenseModel
        fields = '__all__'
        exclude = ['user']
        
        widgets = {
                    'datetime': forms.DateTimeInput(attrs= {'type':'datetime-local'})
                    }