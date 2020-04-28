from django import *
from django.forms import ModelForm
from .models import Gr

class EntryForm(forms.ModelForm):
    class Meta:
        model = Gr
        fields = [
            'gr_number',
            'query_code',
            'name',
            'picture',
            'family_code',
            'section',
            'fee_concession_code',
            'class_of_admission',
            'session_of_admission',
            'current_class',
            'current_session',
            'admission_date',
            'last_school',
            'religion',
            'date_of_birth',
            'active',
        ]


class EntryEditForm(forms.ModelForm):
    class Meta:
        model = Gr
        fields = [
            'gr_number',
            'query_code',
            'name',
            'picture',
            'family_code',
            'fee_concession_code',
            'class_of_admission',
            'session_of_admission',
            'current_class',
            'current_session',
            'admission_date',
            'last_school',
            'religion',
            'date_of_birth',
        ]
