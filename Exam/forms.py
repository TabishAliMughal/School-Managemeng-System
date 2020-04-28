from django import forms
from django.forms import ModelForm
from .models import *


class ExamForm(forms.ModelForm):
    class Meta:
        model = Exam
        fields = {
            'exam_session'
        }
        
class SemesterForm(forms.ModelForm):
    class Meta:
        model = Semester
        fields = {
            'exam_code',
            'semester_code',
            'semester_name'
        }

class SemesterbreakupForm(forms.ModelForm):
    class Meta:
        model = Semesterbreakup
        fields = {
            'exam_code',
            'semester_code',
            'semesterbreakup_code',
            'semesterbreakup_name'
        }

class QuaterForm(forms.ModelForm):
    class Meta:
        model = Quater
        fields = {
            'exam_code',
            'semester_code',
            'semesterbreakup_code',
            'quater_code',
            'quater_name'
        }

class AssesmentForm(forms.ModelForm):
    class Meta:
        model = Assesment
        fields = {
            'exam_code',
            'semester_code',
            'semesterbreakup_code',
            'quater_code',
            'assesment_code',
            'assesment_name'
        }

class MarkForm(forms.ModelForm):
    class Meta:
        model = Mark
        fields = {
            'exam_Gr_no',
            'class_code',
            'subject_code',
            'exam_code',
            'semester_code',
            'semesterbreakup_code',
            'quater_code',
            'assesment_code',
            'total_marks',
            'obtained_marks'
        }