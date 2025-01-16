from django.db import models
from users.models import User
from core.models import Blog

class Reaction(models.Model):
    DoesNotExist = None
    objects = None
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Blog, on_delete=models.CASCADE)
    reaction = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'post', 'reaction')  # A user can react with one type to a post only once

    def __str__(self):
        return self.reaction