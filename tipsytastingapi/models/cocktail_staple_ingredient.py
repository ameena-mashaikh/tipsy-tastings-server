from django.db import models

class CocktailStapleIngredient(models.Model):
    cocktail = models.ForeignKey("Cocktail", on_delete=models.CASCADE, related_name='staples_for_cocktail')
    staple_ingredient = models.ForeignKey("StapleIngredient", on_delete=models.CASCADE, related_name='staple_needed_for_cocktail')
    quantity = models.FloatField(null=True, default=None)

