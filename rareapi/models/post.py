# AUTHOR: JARON LANE

from django.db import models

class Post(models.Model):
    user = models.ForeignKey("RareUser", on_delete=models.CASCADE)
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    publication_date = models.DateTimeField(auto_now=False, auto_now_add=False)
    image_url = models.CharField(max_length=512)
    content = models.CharField(max_length=150)
    approved = models.BooleanField()