
from songs.services.song_service import SongService
from songs.storage.storage_factory import StorageFactory


class SongController:

    def __init__(self):
        self.song_service = SongService()
        self.storage = StorageFactory()



    def upload_song(self, request, user):
        title = request.POST.get("title")
        artist = request.POST.get("artist")
        genre = request.POST.get("genre")
        file = request.FILES.get("file")

        file_path = self.storage.save_audio_file(file)
        song = self.song_service.create_song(
            title,
            artist,
            genre,
            file_path,
            user
        )

        return {
            "id": song.id,
            "title": song.title
        }, 201