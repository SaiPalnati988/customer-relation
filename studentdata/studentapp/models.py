from django.db import models

class StudentData(models.Model):
    name = models.CharField(max_length=50)
    roll_no = models.IntegerField()
    mobile = models.BigIntegerField()
    institute = models.CharField(max_length=50)
    location = models.CharField(max_length=50)

# Create your models here.
