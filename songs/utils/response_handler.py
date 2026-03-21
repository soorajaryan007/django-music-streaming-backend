from django.http import FileResponse, HttpResponseRedirect
from songs.config import Config


class StreamingService:

    def stream_song(self, song_url):

        # Production → redirect to CDN / external URL
        if Config.ENV == "production":
            return HttpResponseRedirect(song_url)

        # Local → serve file
        return FileResponse(
            open(song_url, "rb"),
            content_type="audio/mpeg"
        )