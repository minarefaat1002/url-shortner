from django.db import models

# Create your models here.
class Url(models.Model):
    link = models.CharField(max_length=10000)
    urlId = models.CharField(max_length=10)