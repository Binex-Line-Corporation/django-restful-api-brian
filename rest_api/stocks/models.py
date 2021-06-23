from django.db import models

# Create your models here.

class stocks(models.Model):
    ticker = models.CharField(max_length=4)
    company_name = models.CharField(max_length=100)
    date = models.DateField()
    opening_price = models.FloatField()
    closing_price = models.FloatField()