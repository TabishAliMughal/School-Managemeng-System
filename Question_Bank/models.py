from django.db import models
from dependencies.models import Subject, Class, City
from multiselectfield import MultiSelectField
from django.urls import reverse

# Create your models here.

class Publisher(models.Model):
    publisher_code = models.AutoField(unique = True, primary_key = True)
    publisher_name = models.CharField(max_length=200)
    city = models.ForeignKey(City, on_delete= models.CASCADE, default=1)

    def __str__(self):
        return self.publisher_name

class Book(models.Model):
    MEDIUM_CHOICES = (
        ('English','English'),
        ('Urdu', 'Urdu'),
        ('Sindhi', 'Sindhi')
    )
    book_code = models.AutoField(unique = True, primary_key = True)
    book_name = models.CharField(max_length=200)
    classes = models.ForeignKey(Class, on_delete= models.CASCADE, default=1)
    subject = models.ForeignKey(Subject, on_delete= models.CASCADE, default=1)
    publisher = models.ForeignKey(Publisher, on_delete= models.CASCADE, default=1)
    medium = models.CharField(max_length=10, choices=MEDIUM_CHOICES, default="none")
    def	get_absolute_url(self):
        return reverse('book_detail',args=[self.book_code])
    def __str__(self):
        return self.book_name

class Chapter(models.Model):
    chapter_code = models.AutoField(unique = True, primary_key = True)
    chapter_name = models.CharField(max_length = 200)
    books = models.ForeignKey(Book, on_delete= models.CASCADE, default=1)
    def __str__(self):
        return self.chapter_name

class Question_Type(models.Model):
    Q_type_code = models.AutoField(unique = True, primary_key = True)
    question_type = models.CharField(max_length=200)
    def __str__(self):
        return self.question_type

class Question_Taken(models.Model):
    QUESTION_CHOICES = (
        ('Exercise','Exercise'),
        ('General', 'General')
    )
    question_from = models.CharField(max_length=10, choices=QUESTION_CHOICES, default="none")
    def __str__(self):
        return self.question_from


class Question_Bank(models.Model):
    QUESTION_CHOICES = (
      ('Exercise','Exercise'),
        ('General', 'General')
    )
    question_code = models.AutoField(unique = True, primary_key = True)
    question = models.TextField()
    subject = models.ForeignKey(Subject, on_delete = models.CASCADE, default = 1)
    classes = models.ForeignKey(Class, on_delete = models.CASCADE, default = 1)
    publisher = models.ForeignKey(Publisher, on_delete = models.CASCADE, default = 1)
    book = models.ForeignKey(Book, on_delete = models.CASCADE, default = 1)
    chapter = models.ForeignKey(Chapter, on_delete = models.CASCADE, default = 1)
    question_type = models.ForeignKey(Question_Type, on_delete = models.CASCADE, default = 1)
    questions_from = models.CharField(max_length=10, choices=QUESTION_CHOICES, default="none")
    def	get_absolute_url(self):
        return reverse('question_bank_detail',args=[self.question_code])
    def __str__(self):
        return self.question