from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Actor(models.Model):
    name=models.CharField(max_length=50)

class Film(models.Model):
    title=models.CharField(max_length=50)
    year=models.IntegerField()
    location=models.CharField(max_length=255)
    fact=models.TextField()
    company=models.CharField(max_length=50)
    distributor=models.CharField(max_length=50)
    director=models.CharField(max_length=50)
    writer=models.CharField(max_length=50)
    actors=models.ManyToManyField(Actor)
    latitude=models.FloatField()
    longitude=models.FloatField()