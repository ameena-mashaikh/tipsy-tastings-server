from django.db import models

class CocktailLiqueur(models.Model):
    cocktail = models.ForeignKey("Cocktail", on_delete=models.CASCADE, related_name='liqueur_for_cocktail')
    liqueur = models.ForeignKey("Liqueur", on_delete=models.CASCADE, related_name='liqueur_needed_for_cocktail', blank = True)
