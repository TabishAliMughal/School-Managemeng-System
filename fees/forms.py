from django import *
from django.forms import ModelForm
from .models import *

class ClassFeeForm(forms.ModelForm):
    class Meta:
        model = ClassFee
        fields = [
            'class_fee_code',
            'class_code',
            'fee_type_code',
            'fee_amount',
            'description',
        ]


class FeeDefineForm(forms.ModelForm):
    class Meta:
        model = StFeeDefine
        fields = [
            'fee_def_code',
            'gr_number',
            'fee_type',
            'concession_percent',
        ]


class FeeRegisterForm(forms.ModelForm):
    class Meta:
        model = FeeRegister
        fields = [
            'gr_number',
            'fee_types',
            'fee_amount',
            'month',
            'due_date',
            'paid_amount',
        ]

class DateForm(forms.DateInput):
    Date = forms.DateField()