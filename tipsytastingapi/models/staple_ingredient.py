from django.db import models

class StapleIngredient(models.Model): 
    name = models.CharField(max_length=75)
