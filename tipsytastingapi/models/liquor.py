from django.db import models

class Liquor(models.Model): 
    label = models.CharField(max_length=75)
