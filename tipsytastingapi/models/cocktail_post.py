from django.db import models

class CocktailPost(models.Model):
    name = models.CharField(max_length = 75)
    cocktail = models.ForeignKey("Cocktail", on_delete=models.CASCADE, related_name='post_cocktail')
    caption = models.CharField(max_length = 200)
    mixologist = models.ForeignKey("Mixologist", on_delete=models.CASCADE, related_name='mixologist_post')