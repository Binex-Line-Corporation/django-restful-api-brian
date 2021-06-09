from django.db import models

# Create your models here.

class books(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    first_8_lines = models.CharField(max_length=100)
    published = models.IntegerField()