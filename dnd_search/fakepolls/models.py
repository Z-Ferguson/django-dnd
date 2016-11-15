from django.db import models

# Create your models here.

class Hero(models.Model):
    hero_name = models.CharField(max_length=25)
    race = models.CharField(max_length=20)
    heroclass = models.CharField(max_length=25)
    alignment = models.CharField(max_length=30)
    age = models.IntegerField(default=0)
    height = models.IntegerField(default=0)
    level = models.IntegerField(default=0)
    background = models.CharField(max_length=200)
    faction = models.CharField(max_length=200)

    def __repr__(self):
        return hero_name + " " + race
