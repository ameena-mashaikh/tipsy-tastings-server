from django.db import models
from django.contrib.auth.models import User

class Mixologist(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    member_since = models.DateField(auto_now_add=True)
    image = models.CharField(max_length=513)