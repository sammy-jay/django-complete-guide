from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Board(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.TextField(max_length=100)

    def __str__(self):
        return self.name
    

class Topic(models.Model):
    subject = models.CharField(max_length=100)
    last_updated = models.DateTimeField(auto_now_add=True)
    starter = models.ForeignKey(User, on_delete=models.CASCADE, related_name='topics')
    board = models.ForeignKey("Board", on_delete=models.CASCADE, related_name='topics')

    def __str__(self):
        return self.subject


class Post(models.Model):
    message = models.TextField(max_length=1000)
    topic = models.ForeignKey("Topic", on_delete=models.CASCADE, related_name='posts')
    created_at = models.DateTimeField(auto_now=True)
    update_at = models.DateTimeField(auto_now_add=True,null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    update_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="+")

    def __str__(self):
        return self.message[:10]