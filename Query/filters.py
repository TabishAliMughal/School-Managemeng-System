import django_filters
from .models import Entry_data 

class Query_filter(django_filters.FilterSet):
    class Meta:
        model = Entry_data
        fields = '__all__'