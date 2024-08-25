from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    old = models.IntegerField()
    vacant = models.BooleanField()
    matiereEnseigne = models.CharField(max_length=100)
    prochainCours = models.CharField(max_length=100)
    sujetProchaineReunion = models.CharField(max_length=100)


