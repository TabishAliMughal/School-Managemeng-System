from dependencies.models import *
from dependencies.models import Fee_Concession , Class , School , Section , Family
from django.urls import reverse

class Entry_data(models.Model):
    Gender_Choices = (
        ('M', 'Male'),
        ('FM', 'Female'),
    )
    Query_code = models.AutoField(primary_key=True, unique=True)
    Name = models.CharField(max_length=30, verbose_name="Name")
    father_name = models.CharField(max_length=30, verbose_name="Father")
    Address = models.CharField(max_length=30)
    gender = models.CharField(max_length=10, choices=Gender_Choices, default="none")
    last = models.ForeignKey(Class, on_delete= models.CASCADE, default=1)
    Previous_school = models.ForeignKey(School, on_delete= models.CASCADE, default=1)
    Addmission_required = models.ForeignKey(Class, on_delete= models.CASCADE, related_name='required', default=1)
    Test_performed = models.BooleanField()
    Suggested_class = models.ForeignKey(Class, on_delete= models.CASCADE, related_name='suggested')
    test_teacher = models.CharField(max_length=30)
    date_of_test = models.DateField()
    Fee_type = models.ForeignKey(Fee_Concession, on_delete= models.CASCADE)
    Contact = models.CharField(max_length=20)
    def	get_absolute_url(self):
        return reverse('entry_detail',args=[self.Query_code])
    def __str__(self):
        return self.Name
    class Meta:
        ordering = ('Query_code',)
        index_together = (('Query_code', 'Name'),)


					
