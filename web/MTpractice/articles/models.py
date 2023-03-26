from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=20)
    category = models.CharField(max_length=10, default='')
    content = models.TextField()
    image = models.ImageField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)