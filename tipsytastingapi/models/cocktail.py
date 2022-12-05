from django.db import models

class Cocktail(models.Model):
    name = models.CharField(max_length = 75)
    category = models.ForeignKey("Category", on_delete=models.CASCADE, related_name='cocktail_category')
    recipe = models.CharField(max_length = 800)
    #image = models.CharField(max_length=513) OR models.URLField(max_length=300, blank=True)
    mixologist_id = models.ForeignKey("Mixologist", on_delete=models.CASCADE, related_name='cocktail_mixologist')