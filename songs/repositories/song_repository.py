from songs.models import Song

def get_song_by_id(song_id):
    return Song.objects.filter(id=song_id).first()

class SongRepository:

    def get_song_by_id(self, song_id):
        return Song.objects.filter(id=song_id).first()