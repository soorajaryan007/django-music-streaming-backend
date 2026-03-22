import os
import uuid
from django.conf import settings
from songs.config import Config


class LocalStorage:

    def __init__(self):
        self.upload_folder = Config.UPLOAD_FOLDER
        os.makedirs(self.upload_folder, exist_ok=True)

    def save_audio_file(self, file):
        filename = f"{uuid.uuid4()}.mp3"

        file_path = os.path.join(settings.MEDIA_ROOT, filename)

        with open(file_path, 'wb+') as destination:
            for chunk in file.chunks():
                destination.write(chunk)

        return file_path   # ✅ absolute path
                