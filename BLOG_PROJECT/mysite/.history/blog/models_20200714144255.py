from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def get_approved_comments(self):
        # accessing the
        # the Comment will be comments
        # in this case
        return self.comments.filter(approved_comment=True)

    # this name is fixed
    # it actually shows when the work is finished
    # posted data then where do  you go
    # it goes to the post_detail page with the pk of the post
    # you can do it to other place to
    # def get_absolute_url(self):
    #    return reverse('post_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    # when the work finished go to the
    # post list
    def get_absolute_url(self):
        return reverse('post_list')

    def __str__(self):
        return self.text
