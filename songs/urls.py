from django.urls import path
from . import views
from .views import get_users
urlpatterns = [
    path("songs", views.get_songs),
    path("play/<int:song_id>", views.play_song),
    path("songs/search", views.search_song),
    path("upload-song", views.upload_song),
    path("users", get_users),
]


