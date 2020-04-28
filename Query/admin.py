from django.contrib import admin
from.models import Entry_data

admin.site.register(Entry_data)
class Entry_dataAdmin(admin.ModelAdmin):
    list_display = ('Query_code', 'Name', 'father_name','Address', 'Test_Performed', 'suggested_class', 
'test_teacher', 'date_of_test')
    list_filter = ('Query_code', 'Name')
    search_fields = ('Name','father')