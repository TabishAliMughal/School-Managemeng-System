from django.db import models
from multiselectfield import MultiSelectField
from django.urls import reverse


class Class(models.Model):
    class_code = models.AutoField(primary_key= True, unique = True)
    class_name = models.CharField(max_length = 200)
    remarks = models.TextField()
    def __str__(self):
        return self.class_name

class Family(models.Model):
    family_code = models.AutoField(primary_key = True,unique = True)
    surname = models.CharField(unique = True , max_length = 200)
    father_name = models.CharField(max_length = 200)
    ph_no_father = models.CharField(max_length = 200)
    mother_name = models.CharField(max_length = 200)
    ph_no_mother = models.CharField(max_length = 200)
    address = models.CharField(max_length=200)
    def	get_absolute_url(self):
        return reverse('family_detail',args=[self.family_code])
    def __str__(self):
        return self.surname       

class Fee_Concession(models.Model):
    fee_concession_code = models.AutoField(unique = True , primary_key = True)
    fee_concession_name = models.CharField(max_length=100)
    concession_percent = models.FloatField()
    description = models.TextField()
    def __str__(self):
        return self.fee_concession_name



class School(models.Model):
    school_code = models.AutoField(unique=True, primary_key=True)
    school_name = models.CharField(max_length=200)
    school_area = models.CharField(max_length=200)
    remarks = models.TextField()
    def __str__(self):
        return self.school_name

class Section(models.Model):
    sect_code = models.AutoField(unique=True, primary_key=True)
    sect_name = models.CharField(max_length=200)
    remarks = models.TextField()
    def __str__(self):
        return self.sect_name
        


class Session(models.Model):
    session_code = models.AutoField( primary_key= True, unique= True)
    session_name = models.CharField(max_length = 200)
    def __str__(self):
        return self.session_name

class Religion(models.Model):
    religion_code = models.AutoField(primary_key= True, unique= True)
    religion = models.CharField(max_length = 200)
    def __str__(self):
        return self.religion

class Subject(models.Model):
    subject_code = models.AutoField(primary_key= True, unique= True)
    subjects = models.CharField(max_length = 200)
    def __str__(self):
        return self.subjects

class Class_Subject(models.Model):
    Class_code = models.AutoField(primary_key= True, unique= True)
    Class = models.ForeignKey(Class, on_delete= models.CASCADE, default=1)
    class_subjects = models.ForeignKey(Subject, on_delete = models.CASCADE)
    def	get_absolute_url(self):
        return reverse('class_subject_detail',args=[self.Class_code])
    def __str__(self):
        return str(self.Class)


class Fee_Type(models.Model):
    fee_type_code = models.AutoField(unique=True, primary_key=True)
    fee_type = models.CharField(max_length=200)
    description = models.TextField()
    def __str__(self):
        return self.fee_type

class Month(models.Model):
    month_code= models.AutoField(unique=True, primary_key=True)
    months = models.CharField(max_length=200)
    def __str__(self):
        return self.months


class City(models.Model):
    city_code = models.AutoField(unique = True, primary_key = True)
    cities = models.CharField(max_length=200)
    def __str__(self):
        return self.cities