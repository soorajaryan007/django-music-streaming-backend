import os
from django.http import HttpResponseNotFound
from django.http import FileResponse, HttpResponseRedirect

from songs.config import Config

class StreamingService:

    def stream_song(self, song_url):

        if Config.ENV == "production":
            return HttpResponseRedirect(song_url)

        if not os.path.exists(song_url):
            return HttpResponseNotFound("File not found ❌")

        return FileResponse(
            open(song_url, "rb"),
            content_type="audio/mpeg"
        )