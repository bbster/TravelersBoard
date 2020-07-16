from django.db import models
from django.db.models import CASCADE
from apps.account.models import User


class Board(models.Model):
    unique_title = models.CharField(unique=True, max_length=100)

    creator = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='boards')
    create_date = models.DateTimeField(auto_now_add=True, editable=False)
    modify_date = models.DateTimeField(auto_now=True, blank=True, null=True, editable=False)

    def __str__(self):
        return self.unique_title


class Post(models.Model):
    board = models.ForeignKey('board.Board', on_delete=CASCADE, related_name='posts')
    title = models.CharField(max_length=50, blank=True, null=True)
    content = models.TextField(null=True, blank=True)

    creator = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='posts')
    create_date = models.DateTimeField(auto_now_add=True, editable=False)
    modify_date = models.DateTimeField(auto_now=True, blank=True, null=True, editable=False)

    def __str__(self):
        return self.title + self.creator.username


class Comment(models.Model):
    post = models.ForeignKey(Post, null=True, blank=True, on_delete=models.CASCADE, related_name='comments')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='childs')
    content = models.TextField(null=True, blank=True)

    creator = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='comments')
    create_date = models.DateTimeField(auto_now_add=True, editable=False)
    modify_date = models.DateTimeField(auto_now=True, blank=True, null=True, editable=False)

    def __str__(self):
        return self.content + self.creator.username
