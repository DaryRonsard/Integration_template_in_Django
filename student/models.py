from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    old = models.IntegerField()
    classe = models.CharField(max_length=100)
    identify = models.CharField(max_length=100)
    classeroom = models.CharField(max_length=100)
    identify = models.CharField(max_length=100)