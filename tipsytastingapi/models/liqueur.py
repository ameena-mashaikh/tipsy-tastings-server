from django.db import models

class Liqueur(models.Model): 
    name = models.CharField(max_length=75)
