from django import forms
from django.forms import ModelForm
from .models import *

class Attendence_Form(forms.ModelForm):
    class Meta:
        model = SaveAttendence
        fields = [
            'gr' ,
            'family' ,
            'classes' ,
            'sections' ,
            'attendence' ,
            'date' ,
        ]
