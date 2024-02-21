from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=50)
    age=models.IntegerField()
    marks=models.IntegerField()
    avg=models.FloatField()
    email=models.EmailField()