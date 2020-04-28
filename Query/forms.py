from django import forms
from django.forms import ModelForm
from .models import Entry_data

class Form(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(Form, self).__init__(*args, **kwargs)
        self.fields['date_of_test'].widget.attrs.update({
            'id': 'datepicker',
        })
    class Meta:
        model = Entry_data
        fields = {
            'Name',
            'father_name',
            'Address',
            'gender',
            'last',
            'Previous_school',
            'Addmission_required',
            'Test_performed',
            'Suggested_class',
            'test_teacher',
            'date_of_test',
            'Fee_type',
            'Contact',
        }
        
