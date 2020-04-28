from django.db import models
from django.urls import reverse

class UserType(models.Model):
    TypeCode = models.AutoField(primary_key = True , unique = True )
    Usertype = models.CharField(max_length = 50)
    def __str__(self):
        return self.Usertype

class UserProfile(models.Model):
    UserCode = models.AutoField(primary_key = True , unique = True )
    Usertype = models.ForeignKey(UserType,on_delete = models.CASCADE)
    Name = models.CharField(max_length = 50)
    Father = models.CharField(max_length = 50)
    Address = models.CharField(max_length = 200)
    Mobile = models.CharField(max_length = 11)
    Email = models.EmailField()
    Password = models.CharField(max_length = 25)
    def __str__(self):
        return self.Name
    def get_absolute_url(self):
        return reverse('userprofiledetail_url',args=[self.UserCode])
