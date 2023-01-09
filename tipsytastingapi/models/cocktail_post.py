from django.db import models

class CocktailPost(models.Model):
    cocktail = models.ForeignKey("Cocktail", on_delete=models.CASCADE, related_name='post_cocktail')
    caption = models.CharField(max_length = 200)
    liked_users = models.ManyToManyField("Mixologist", through = "Likes")