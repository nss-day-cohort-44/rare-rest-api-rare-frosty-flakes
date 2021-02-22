from django.db import models

class Post(models.Model):
    user = models.ForeignKey("RareUser", on_delete=models.CASCADE)
    category = models.ForeignKey("Category", verbose_name=_(""), on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    publication_date = models.DateTimeField(auto_now=False, auto_now_add=False)
    models.ImageField(upload_to="photos", max_length=None)
    content = models.CharField(max_length=150)
    approved = models.BooleanField()