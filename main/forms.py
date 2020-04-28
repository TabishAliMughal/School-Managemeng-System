from django import forms
from django.forms import ModelForm
from .models import *


class UserTypeForm(forms.ModelForm):
    class Meta:
        model = UserType
        fields = [
            'Usertype',
        ]


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = [
            'Usertype',
            'Name',
            'Father',
            'Address',
            'Mobile',
            'Email',
            'Password',
        ]