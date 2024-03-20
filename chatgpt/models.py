from django.db import models
from users.models import User

class ChatgptHistory(models.Model):
    user_id = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name='userId',
    )
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    message = models.CharField(max_length=2000)
    response_message = models.CharField(max_length=2000)
