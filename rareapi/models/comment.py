""" 
Created By: Danny McCracken
Date: 2/22/21
Subject: Defines model for each comment
"""

from django.db import models


class Comment(models.Model):

    post = models.ForeignKey("Post", on_delete=models.CASCADE)
    content = models.CharField(max_length=500)
    author = models.ForeignKey("RareUser", on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now=False, auto_now_add=False)
    @property
    def joined(self):
        return self.__joined

    @joined.setter
    def joined(self, value):
        self.__joined = value
