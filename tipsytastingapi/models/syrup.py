from django.db import models

class Syrup(models.Model): 
    name = models.CharField(max_length=75)
