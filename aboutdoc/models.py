from django.db import models

class Document(models.Model):

    label = models.TextField()
    # file = models.FieldFile(upload_to='uploads/')

    
    