from django import forms
from django.forms import ModelForm
from .models import Book, Publisher, Chapter, Question_Type, Question_Bank


class book_form(forms.ModelForm):
    class Meta:
        model = Book
        fields = {
            'book_code',
            'book_name',
            'classes',
            'subject',
            'publisher',
            'medium'
        }

        
class publisher_form(forms.ModelForm):
    class Meta:
        model = Publisher
        fields = {
            'publisher_code',
            'publisher_name',
            'city'
        }

class chapter_form(forms.ModelForm):
    class Meta:
        model = Chapter
        fields = {
            'chapter_code',
            'chapter_name',
            'books'
        }


class question_type_form(forms.ModelForm):
    class Meta:
        model = Question_Type
        fields = {
            'Q_type_code',
            'question_type'
        }


class question_bank_form(forms.ModelForm):
    class Meta:
        model = Question_Bank
        fields = {
            'question_code',
            'question',
            'subject',
            'classes',
            'publisher',
            'book',
            'chapter',
            'question_type',
            'questions_from'
        }