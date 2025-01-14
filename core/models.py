from django.db import models
from users.models import User

# Create your models here.
class Blog(models.Model):
    DoesNotExist = None
    objects = None
    title = models.CharField(max_length=50)
    slug = models.CharField(null=True,  blank=True, max_length=100)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    published_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title