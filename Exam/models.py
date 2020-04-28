from django.db import models
from django.utils import timezone
from dependencies.models import *
from student_information.models import *
from django.urls import reverse

class Exam(models.Model):
    exam_code = models.AutoField(primary_key=True, unique=True)
    exam_session = models.ForeignKey(Session, on_delete= models.CASCADE)
    def	get_absolute_url(self):
        return reverse('exam_detail',args=[self.exam_code])
    def __str__(self):
        return str(self.exam_session)


class Semester(models.Model):
    exam_code = models.ForeignKey(Exam, on_delete= models.CASCADE)
    semester_code = models.AutoField(primary_key=True, unique=True)
    semester_name = models.CharField(max_length=30, verbose_name="semester")
    def __str__(self):
        return self.semester_name
    def	get_absolute_url(self):
        return reverse('semester_detail',args=[self.semester_code])

class Semesterbreakup(models.Model):
    exam_code = models.ForeignKey(Exam, on_delete= models.CASCADE)
    semester_code = models.ForeignKey(Semester, on_delete= models.CASCADE)    
    semesterbreakup_code = models.AutoField(primary_key=True, unique=True)
    semesterbreakup_name = models.CharField(max_length=30, verbose_name="semester-breakup")
    def __str__(self):
        return self.semesterbreakup_name
    def	get_absolute_url(self):
        return reverse('semesterB_detail',args=[self.semesterbreakup_code])

class Quater(models.Model):
    exam_code = models.ForeignKey(Exam, on_delete= models.CASCADE)
    semester_code = models.ForeignKey(Semester, on_delete= models.CASCADE)
    semesterbreakup_code = models.ForeignKey(Semesterbreakup, on_delete= models.CASCADE)    
    quater_code = models.AutoField(primary_key=True, unique=True)
    quater_name = models.CharField(max_length=30, verbose_name="Quater")
    def __str__(self):
        return self.quater_name
    def	get_absolute_url(self):
        return reverse('quater_detail',args=[self.quater_code])

class Assesment(models.Model):
    exam_code = models.ForeignKey(Exam, on_delete= models.CASCADE)
    semester_code = models.ForeignKey(Semester, on_delete= models.CASCADE)
    semesterbreakup_code = models.ForeignKey(Semesterbreakup, on_delete= models.CASCADE)
    quater_code = models.ForeignKey(Quater, on_delete= models.CASCADE)    
    assesment_code = models.AutoField(primary_key=True, unique=True)
    assesment_name = models.CharField(max_length=30, verbose_name="Quater")
    def __str__(self):
        return self.assesment_name
    def	get_absolute_url(self):
        return reverse('assesment_detail',args=[self.assesment_code])

class Mark(models.Model):
    id = models.AutoField(primary_key = True , unique = True)
    exam_Gr_no = models.ForeignKey(Gr, on_delete= models.CASCADE, related_name='number')
    class_code = models.ForeignKey(Class, on_delete= models.CASCADE)
    subject_code = models.ForeignKey(Subject, on_delete= models.CASCADE)
    exam_code = models.ForeignKey(Exam, on_delete= models.CASCADE)
    semester_code = models.ForeignKey(Semester, on_delete= models.CASCADE)
    semesterbreakup_code = models.ForeignKey(Semesterbreakup, on_delete= models.CASCADE)
    quater_code = models.ForeignKey(Quater, on_delete= models.CASCADE)    
    assesment_code = models.ForeignKey(Assesment, on_delete= models.CASCADE)
    total_marks = models.CharField(max_length=30, verbose_name="total_marks")
    obtained_marks = models.CharField(max_length=30, verbose_name="obtained_marks")
    def __str__(self):
        return str(self.exam_Gr_no)
    def	get_absolute_url(self):
        return reverse('mark_detail',args=[self.id])
   
