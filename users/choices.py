from django.db import models


class Role(models.TextChoices):
    CUSTOMER = 'Customer'
    ADMIN = 'Admin'
