import os
import uuid
from songs.config import Config


class LocalStorage:

    def __init__(self):
        self.upload_folder = Config.UPLOAD_FOLDER
        os.makedirs(self.upload_folder, exist_ok=True)

    def save_audio_file(self, file):
        filename = f"{uuid.uuid4()}.mp3"
        file_path = os.path.join(self.upload_folder, filename)

        with open(file_path, 'wb+') as destination:
            for chunk in file.chunks():
                destination.write(chunk)

        return file_path
        