from django.db import models
from student_information.models import *
from dependencies.models import *


# Create your models here. 
class SaveAttendence(models.Model):
    code = models.AutoField(primary_key = True)
    gr = models.ForeignKey(Gr, on_delete = models.CASCADE)
    family = models.ForeignKey(Family, on_delete = models.CASCADE)
    classes = models.ForeignKey(Class, on_delete = models.CASCADE)
    sections = models.ForeignKey(Section, on_delete = models.CASCADE)
    attendence = models.CharField(max_length = 20)
    date = models.DateField()
    # def __str__(self):
    #     return str(self.gr) , self.attendence
