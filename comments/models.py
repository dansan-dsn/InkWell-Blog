from django.db import models
from users.models import User
from core.models import Blog

# Create your models here.
class Comments(models.Model):
    DoesNotExist = None
    objects = None
    content = models.TextField()
    commenter = models.ForeignKey(User, on_delete=models.CASCADE)
    blog_post = models.ForeignKey(Blog, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content