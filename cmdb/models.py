from django.db import models

# Create your models here.
class User_Info(models.Model):
    name = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    age = models.CharField(max_length=20)
    email = models.EmailField()
    city = models.CharField(max_length=30)
    text = models.TextField()
