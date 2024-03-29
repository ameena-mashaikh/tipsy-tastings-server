from django.db import models
from cloudinary.models import CloudinaryField

class Cocktail(models.Model):
    name = models.CharField(max_length = 75)
    category = models.ForeignKey("Category", on_delete=models.CASCADE, related_name='cocktail_category')
    recipe = models.CharField(max_length = 800)
    image = models.CharField(max_length=513)
    date = models.DateTimeField(auto_now_add=True)
    created_by_mixologist = models.ForeignKey("Mixologist", on_delete=models.CASCADE, related_name='cocktail_mixologist')
    liquors = models.ManyToManyField("Liquor", through = "CocktailLiquor")
    liqueurs = models.ManyToManyField("Liqueur", through = "CocktailLiqueur")
    staple_ingredients = models.ManyToManyField("StapleIngredient", through = "CocktailStapleIngredient")
    syrups = models.ManyToManyField("Syrup", through = "CocktailSyrup")