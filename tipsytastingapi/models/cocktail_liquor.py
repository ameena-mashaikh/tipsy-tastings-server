from django.db import models

class CocktailLiquor(models.Model):
    cocktail = models.ForeignKey("Cocktail", on_delete=models.CASCADE, related_name='liquor_for_cocktail')
    liquor = models.ForeignKey("Liquor", on_delete=models.CASCADE, related_name='liquor_needed_for_cocktail')
    quantity = models.FloatField(default=None)
