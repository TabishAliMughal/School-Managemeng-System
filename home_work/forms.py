from django import forms
from django.forms import ModelForm
from .models import home_work

class home_work_form(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(home_work_form, self).__init__(*args, **kwargs)
        self.fields['date'].widget.attrs.update({
            'id': 'datepicker',
        })
    class Meta:
        model = home_work
        fields = {
            'classes', 
            'sections', 
            'teacher',
            'subjects', 
            'chapter', 
            'page', 
            'descriptions',
            'date'
        }
