from django.db import models

# Create your models here.

from django.db import models

class Customer(models.Model):
    phone_no = models.CharField(max_length=10)
    password = models.CharField(max_length=50)
