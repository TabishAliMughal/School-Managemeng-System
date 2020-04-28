from django import forms
from django.forms import ModelForm
from .models import Class, School, Family, Fee_Concession, Section, Session, Religion, Subject, Class_Subject, Fee_Type, Month, City

class class_form(forms.ModelForm):
    class Meta:
        model = Class
        fields = {
            'class_code',
            'class_name',
            'remarks'
        }

class school_form(forms.ModelForm):
    class Meta:
        model = School
        fields = {
            'school_code',
            'school_name',
            'school_area',
            'remarks'
        }

class family_form(forms.ModelForm):
    class Meta:
        model = Family
        fields = {
            'family_code',
            'surname',
            'father_name',
            'ph_no_father',
            'mother_name',
            'ph_no_mother',
            'address'
        }

class fee_concession_form(forms.ModelForm):
    class Meta:
        model = Fee_Concession
        fields = {
            'fee_concession_code',
            'fee_concession_name',
            'concession_percent',
            'description'
        }

class section_form(forms.ModelForm):
    class Meta:
        model = Section
        fields = {
            'sect_code',
            'sect_name',
            'remarks'
        }

class session_form(forms.ModelForm):
    class Meta:
        model = Session
        fields = {
            'session_code',
            'session_name'
        }

class religion_form(forms.ModelForm):
    class Meta:
        model = Religion
        fields = {
            'religion_code',
            'religion'
        }


class subject_form(forms.ModelForm):
    class Meta:
        model = Subject
        fields = {
            'subject_code',
            'subjects'
        }


class classes_subject_form(forms.ModelForm):
    class Meta:
        model = Class_Subject
        fields = {
            'Class_code',
            'Class',
            'class_subjects'
        }


class fee_type_form(forms.ModelForm):
    class Meta:
        model = Fee_Type
        fields = {
            'fee_type_code',
            'fee_type',
            'description'
        }


class month_form(forms.ModelForm):
    class Meta:
        model = Month
        fields = {
            'month_code',
            'months'
        }


class city_form(forms.ModelForm):
    class Meta:
        model = City
        fields = {
            'city_code',
            'cities'
        }