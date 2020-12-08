from  django import forms
from  django.forms import ModelForm
from .models import  *
from django.contrib.auth.forms import  UserCreationForm
from  django.contrib.auth.models import User



class OpportunityForm(forms.ModelForm):
    class Meta:
        model=Opportunity
        fields=('name',"amount",'account','stage')

        def __init__(self, *args, **kwargs):
            super(OpportunityForm, self).__init__(*args, **kwargs)
            self.fields['account'].empty_label = "select"

class AccountForm(forms.ModelForm):
    class Meta:
        model=Account
        fields='__all__'



class UserRegisterForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']