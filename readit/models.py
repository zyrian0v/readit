from django.db import models
from django.contrib.auth.models import User

class Board(models.Model):
        name = models.SlugField()
        title = models.CharField(max_length=200)

        def __str__(self):
                return self.name

class Post(models.Model):
        user = models.ForeignKey(User, on_delete=models.CASCADE)
        board = models.ForeignKey(Board, on_delete=models.CASCADE)
        title = models.CharField(max_length=200)
        url = models.URLField()
        description = models.TextField(blank=True)
        votes = models.IntegerField(default=0)

        def __str__(self):
                return self.title

class Comment(models.Model):
        user = models.ForeignKey(User, on_delete=models.CASCADE)
        post = models.ForeignKey(Post, on_delete=models.CASCADE)
        parent = models.ForeignKey("Comment", null=True, blank=True, on_delete=models.CASCADE)
        content = models.TextField()

        def __str__(self):
                return f"({self.post.title}) {self.content}"

