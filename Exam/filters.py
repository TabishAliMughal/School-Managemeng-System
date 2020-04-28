import django_filters
from .models import Mark, Exam, Semesterbreakup, Semester,Quater,Assesment


class Mark_filter(django_filters.FilterSet):
    class Meta:
        model = Mark
        fields = '__all__'

class Exam_filter(django_filters.FilterSet):
    class Meta:
        model = Exam
        fields = '__all__'

class Semester_filter(django_filters.FilterSet):
    class Meta:
        model = Semester
        fields = '__all__'

class Semesterbreakup_filter(django_filters.FilterSet):
    class Meta:
        model = Semesterbreakup
        fields = '__all__'

class Quater_filter(django_filters.FilterSet):
    class Meta:
        model = Quater
        fields = '__all__'

class Assesment_filter(django_filters.FilterSet):
    class Meta:
        model = Assesment
        fields = '__all__'