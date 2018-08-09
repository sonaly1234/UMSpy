from django.db import models

# Create your models here.

class User(models.Model):
    UserName = models.CharField(max_length=20)
    Password = models.CharField(max_length=15)
    Role = models.CharField(max_length=20)
    FirstName = models.CharField(max_length=15)
    LastName = models.CharField(max_length=15)
    Email = models.EmailField(max_length=25)
    Phone = models.CharField(max_length=10)
    EmpId = models.CharField(max_length=10)
    Address = models.TextField
    Pin = models.CharField(max_length=6)

