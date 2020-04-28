from django.db import models
from dependencies.models import *
from Query.models import *
from django.urls import reverse


class Gr(models.Model):
    gr_number = models.IntegerField(auto_created=True , unique = True , primary_key = True)
    query_code = models.OneToOneField(Entry_data , on_delete= models.CASCADE , blank=True , null=True)
    name = models.CharField(max_length = 200)
    picture = models.ImageField(upload_to='images/%Y/%m/%d',blank=True)
    family_code = models.ForeignKey(Family , on_delete= models.CASCADE)
    section = models.ForeignKey(Section , on_delete= models.CASCADE)
    fee_concession_code = models.ForeignKey(Fee_Concession , on_delete= models.CASCADE)
    class_of_admission = models.ForeignKey(Class , on_delete= models.CASCADE , related_name= 'admission_class')
    session_of_admission = models.ForeignKey(Session , on_delete= models.CASCADE , related_name= 'session_of_admission')
    current_class = models.ForeignKey(Class , max_length = 15 , on_delete= models.CASCADE , related_name= 'current_class')
    current_session = models.ForeignKey(Session , on_delete= models.CASCADE , related_name= 'current_session')
    admission_date = models.DateField()
    last_school = models.ForeignKey(School , on_delete = models.CASCADE)
    religion = models.ForeignKey(Religion,on_delete = models.CASCADE)
    date_of_birth = models.DateField()
    active = models.BooleanField()
    def get_absolute_url(self):
        return reverse('gr_detail',args=[self.gr_number])
    def __str__(self):
        return str(self.name)