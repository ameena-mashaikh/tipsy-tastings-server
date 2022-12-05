from django.db import models

class Likes(models.Model):
    cocktail_post = models.ForeignKey("Cocktail", on_delete=models.CASCADE, related_name='post_cocktail_comment')
    mixologist = models.ForeignKey("Mixologist", on_delete=models.CASCADE, related_name='mixologist_comment')
