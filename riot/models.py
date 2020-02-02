from django.db import models

# Create your models here.

class Char(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    skills = models.CharField(max_length=100)


class LorRanked(models.Model):
    name = models.CharField(max_length=100)
    rank = models.IntegerField(null=True,blank=True)

class Region(models.Model):
    name = models.CharField(max_length=20)
    lor_ranked = models.ManyToManyField(LorRanked,null=True,blank=True)





