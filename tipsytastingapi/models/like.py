from django.db import models

class Likes(models.Model):
    cocktail_post = models.ForeignKey("CocktailPost", on_delete=models.CASCADE)
    mixologist = models.ForeignKey("Mixologist", on_delete=models.CASCADE)
