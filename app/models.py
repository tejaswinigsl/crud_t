# Create your models here.
from django.db import models

class Employee1(models.Model):
    empid=models.IntegerField()
    name=models.CharField(max_length=100)
    phone =models.IntegerField()
    age=models.IntegerField()
    email=models.EmailField()
    
