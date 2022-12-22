from django.db import models

# Create your models here.
class User(models.Model):
    fname = models.CharField(max_length=200)
    lname = models.CharField(max_length=200)
    email = models.EmailField(max_length = 254)
    password = models.CharField(max_length=100)
    