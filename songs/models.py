from django.db import models
from users.models import User

class Song(models.Model):
    title = models.CharField(max_length=200)
    artist = models.CharField(max_length=200, blank=True, null=True)
    genre = models.CharField(max_length=100, blank=True, null=True)
    mp3_path = models.CharField(max_length=300)
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE,null=True)  
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title