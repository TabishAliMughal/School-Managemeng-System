import django_filters
from .models import Question_Bank


class Question_Bank_filter(django_filters.FilterSet):
    class Meta:
        model = Question_Bank
        fields = [
            'question_code',
            'question',
            'subject',
            'classes',
            'publisher',
            'book',
            'chapter',
            'question_type',
            'questions_from',
        ]
