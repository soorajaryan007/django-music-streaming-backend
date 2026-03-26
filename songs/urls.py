from django.urls import path
from . import views

urlpatterns = [
    # 🎵 Core APIs
    path("songs/", views.get_songs),
    path("play/<int:song_id>/", views.play_song),
    path("upload-song/", views.upload_song),

    # 🔍 Search APIs (Versioned)
    path("api/v1/search/", views.search_song),           # keyword search
    path("api/v2/search/", views.natural_search_song),   # AI search
]