from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User


class Post(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='post_author')
    title = models.CharField(max_length=200)
