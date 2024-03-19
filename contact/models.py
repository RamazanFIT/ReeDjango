from django.db import models
from users.models import User

class Message(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    telephone = models.CharField(max_length=255)
    message = models.CharField(max_length=2500)
    sender = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='sent_messages')
    receiver = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='received_messages')
