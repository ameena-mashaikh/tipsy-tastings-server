from django.db import models
from django.contrib.auth.models import User

class Mixologist(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    bio = models.CharField(max_length=500)
    image = models.CharField(max_length=513)