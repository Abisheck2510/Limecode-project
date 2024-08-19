from django.db import models

# Create your models here.

class Customer(models.Model):
    buyername = models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    email=models.EmailField()
    phonenumber=models.IntegerField()
