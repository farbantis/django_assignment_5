from django.contrib.auth.models import AbstractUser
from django.db import models


class TaskUser(AbstractUser):
    """just modified user"""


class Note(models.Model):
    text = models.TextField()
    created_at = models.DateTimeField()
    author = models.ForeignKey(TaskUser, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.author} at {self.created_at}'




