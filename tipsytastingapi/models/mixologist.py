from django.db import models
from django.contrib.auth.models import User

class Mixologist(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    member_since = models.DateField(auto_now_add=True)
    #profile_img = models.CharField(max_length=513) OR models.URLField(max_length=300, blank=True)