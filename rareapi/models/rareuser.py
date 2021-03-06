from django.db import models
from django.contrib.auth.models import User

class RareUser(models.Model):

    
    bio = models.CharField(max_length=100)
    profile_image_url = models.CharField(max_length=512)
    created_on = models.DateTimeField(auto_now=False, auto_now_add=False)
    active = models.BooleanField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)
