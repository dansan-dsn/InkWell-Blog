from django.db import models

# Create your models here.
class Categories(models.Model):
    DoesNotExist = None
    objects = None
    name = models.CharField(max_length=50, unique=True)
    slug = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name