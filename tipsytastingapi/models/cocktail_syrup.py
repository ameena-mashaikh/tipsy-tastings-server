from django.db import models

class CocktailSyrup(models.Model):
    cocktail = models.ForeignKey("Cocktail", on_delete=models.CASCADE, related_name='syrup_for_cocktail')
    syrup = models.ForeignKey("Syrup", on_delete=models.CASCADE, related_name='syrup_needed_for_cocktail', blank = True)
