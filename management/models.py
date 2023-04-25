from django.db import models

# Create your models here.

class management_registration(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    phonenumber = models.PositiveBigIntegerField(null=True)
    city = models.CharField(max_length=200, null=True)
    password = models.CharField(max_length=200)