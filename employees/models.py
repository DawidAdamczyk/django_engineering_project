from django.db import models
from django.contrib.auth.models import User
from cars.models import Car

class Employee(models.Model):
    position = models.CharField(max_length=50)
    age = models.PositiveSmallIntegerField()
    sex = models.CharField(max_length=6)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, null='true', on_delete=models.CASCADE)
