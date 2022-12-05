from django.db import models

class Liquor(models.Model): 
    name = models.CharField(max_length=75)
    #image = models.CharField(max_length=513) OR models.URLField(max_length=300, blank=True)
