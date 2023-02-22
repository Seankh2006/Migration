from django.db import models
from django.forms import DurationField

# Create your models here.

class Flight(models.Model):
    origin = models.CharField(max_length=64)
    destination = models.CharField(max_length=64)
    duration = models.IntegerField()


