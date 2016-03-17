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

    def to_dict(self):
        item={}
        item['title']=self.title
        item['year']=self.year
        item['fact']=self.fact
        item['location']=self.location
        item['company']=self.company
        item['distributor']=self.distributor
        item['director']=self.director
        item['writer']=self.writer
        item['longitude']=self.longitude
        item['latitude']=self.latitude