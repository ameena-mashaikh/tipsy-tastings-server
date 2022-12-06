from django.db import models

class Comments(models.Model):
    content = models.CharField(max_length = 200)
    cocktail_post = models.ForeignKey("CocktailPost", on_delete=models.CASCADE)
    mixologist = models.ForeignKey("Mixologist", on_delete=models.CASCADE)
