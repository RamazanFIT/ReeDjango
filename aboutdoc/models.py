from django.db import models

class Document(models.Model):

    label = models.TextField()
    file = models.FileField(upload_to='uploads/')

