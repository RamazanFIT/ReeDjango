from django.db import models


class News(models.Model):
    title = models.CharField(max_length=1000)
    main_photo = models.ImageField(upload_to='news/photos/')
    text = models.TextField()
    video = models.FileField(upload_to='news/videos/', default=None, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class AdditionalPhotosOfNews(models.Model):
    fk = models.ForeignKey(
        to=News,
        on_delete=models.CASCADE,
        related_name='additionalPhotos',
    )
    photo = models.ImageField(upload_to='news/additional-photos/')
    
    
    

