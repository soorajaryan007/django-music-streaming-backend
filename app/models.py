from django.db import models

class User(models.Model):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=120, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username


class Song(models.Model):
    title = models.CharField(max_length=200)
    artist = models.CharField(max_length=200, blank=True, null=True)
    genre = models.CharField(max_length=100, blank=True, null=True)
    mp3_path = models.CharField(max_length=300)  # local file path
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title