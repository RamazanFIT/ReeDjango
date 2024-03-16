from django.db import models
from django.contrib.auth.models import AbstractUser


# class Test(models.Model):

#     name = models.CharField(max_length=255)
#     surname = models.CharField(max_length=255)
#     age = models.IntegerField()
    
    

# class Test2(models.Model):

#     nam2 = models.CharField(max_length=255)
#     surname2 = models.CharField(max_length=255)
#     age2 = models.IntegerField()

class User(AbstractUser):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    username = models.CharField(max_length=255, unique=True)
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []
    
