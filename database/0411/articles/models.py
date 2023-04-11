from django.db import models
from imagekit.processors import Thumbnail, ResizeToFill, SmartResize
from imagekit.models import ProcessedImageField, ImageSpecField

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    image = models.ImageField(blank=True, null=True)
    image_thumbnail =ImageSpecField(
        source = 'image',
        processors=[SmartResize(200, 300)], # 200 X 300으로 줄임
        format = 'JPEG',
        options={
            'quality':80,
        }
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.id}번째글 - {self.title}'
    
class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    parent  = models.ForeignKey(
        'self', 
        on_delete   =models.CASCADE, 
        null        =True, 
        related_name='replies',
    )


