from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.
class Tweet(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='tweets')
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
