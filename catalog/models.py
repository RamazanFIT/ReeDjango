from django.db import models

# Create your models here.
class Catalog(models.Model):

    name = models.TextField()
    file = models.FileField(upload_to='catalogs/')

    
class Reestr(models.Model):

    name = models.TextField()
    file = models.FileField(upload_to='catalogs/')

class PoiskPravoobladateley(models.Model):

    name = models.TextField()
    file = models.FileField(upload_to='catalogs/')


class InostrannyeOkupy(models.Model):

    text = models.TextField()
    title = models.CharField(max_length=255)
    