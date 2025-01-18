from django.db import models
from core.models import Blog

# Create your models here.
class Media(models.Model):
    objects = None,
    DoesNotExist = None,
    post = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='uploads')
    file = models.FileField(upload_to='uploads/')
    media_type = models.CharField(max_length=10, choices=[
        ('image', 'Image'),
        ('video', 'Video'),
    ])
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.media_type