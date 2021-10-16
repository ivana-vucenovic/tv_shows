from django.db import models

class Book(models.Model):
    title=models.CharField(max_length = 255)
    network = models.CharField(max_length = 255)
    release_date = models.DateField()

# Create your models here.
