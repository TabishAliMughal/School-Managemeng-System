from django.db import models
from dependencies.models import *

# Create your models here.
class home_work(models.Model):
    homework_ID = models.AutoField(primary_key = True , unique = True)
    classes = models.ForeignKey(Class, on_delete = models.CASCADE)
    sections = models.ForeignKey(Section, on_delete = models.CASCADE)
    teacher = models.CharField(max_length = 30)
    subjects = models.ForeignKey(Subject, on_delete = models.CASCADE)
    chapter = models.CharField(max_length = 50)
    page = models.IntegerField()
    descriptions = models.CharField(max_length = 300)
    date = models.DateField()
    
    def __str__(self):
        return str(self.classes)