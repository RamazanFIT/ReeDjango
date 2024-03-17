from django.db import models

class Message(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    telephone = models.CharField(max_length=255)
    message = models.CharField(max_length=2500)
    