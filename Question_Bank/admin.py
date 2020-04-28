from django.contrib import admin
from .models import Publisher, Book, Chapter, Question_Type, Question_Taken, Question_Bank

# Register your models here.


admin.site.register(Publisher)
admin.site.register(Book)
admin.site.register(Chapter)
admin.site.register(Question_Type)
admin.site.register(Question_Taken)
admin.site.register(Question_Bank)