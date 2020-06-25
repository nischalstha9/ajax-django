from django.db import models
from django.utils import timezone

# Create your models here.

class Employee(models.Model):
    name = models.CharField(max_length=200)
    contact = models.IntegerField()
    email = models.EmailField( max_length=254)
    address = models.CharField(max_length=200)
    role = models.CharField(max_length=200)
        
    def __str__(self):
        return self.name