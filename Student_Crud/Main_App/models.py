from django.db import models

# Create your models here.
class Student_Details(models.Model):
    roll_no = models.IntegerField()
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    city = models.CharField(max_length=255)
    
    class Meta:
        db_table = 'student_details'