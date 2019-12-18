from django.db import models

class Car(models.Model):
    brand = models.CharField(max_length=40)
    name = models.CharField(max_length=40)
    country = models.CharField(max_length=50)
    year = models.PositiveSmallIntegerField()