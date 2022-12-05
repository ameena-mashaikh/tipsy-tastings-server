from django.db import models

class CocktailStapleIngredients(models.Model):
    cocktail = models.ForeignKey("Cocktail", on_delete=models.CASCADE, related_name='staples_for_cocktail')
    staple_ingredients = models.ForeignKey("StapleIngredients", on_delete=models.CASCADE, related_name='staple_needed_for_cocktail')
