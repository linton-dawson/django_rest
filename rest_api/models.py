from django.db import models
from rest_framework import serializers

# Create your models here.
class Slot1(models.Model):
    invalid_trigger = models.CharField(max_length = 200,default=None)
    values = models.CharField(max_length=1000)
    supported_values = models.CharField(max_length=200,default=None)
    support_multiple = models.BooleanField(default=True)
    key = models.CharField(max_length=200,default=None)
    pick_first = models.BooleanField(default=False)

class Slot2(models.Model):
    invalid_trigger = models.CharField(max_length = 200,default=None)
    key = models.CharField(max_length=200,default=None)
    support_multiple = models.BooleanField(default=True)
    pick_first = models.BooleanField(default=False)
    type = models.CharField(max_length= 1000)
    constraint = models.CharField(max_length= 500,default=None)
    var_name = models.CharField(max_length= 10,default=None)
    values = models.CharField(max_length= 1000)