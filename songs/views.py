import logging

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser

from songs.services.song_service import SongService
from songs.services.song_upload import SongController
from songs.utils.response_handler import StreamingService
from songs.api_latency.latency import measure_latency


logger = logging.getLogger(__name__)

s = SongService()
u = SongController()
st = StreamingService()


# 🎵 Get all songs (public)
@api_view(['GET'])
@permission_classes([AllowAny])
def get_songs(request):
    songs = s.get_all_songs()
    return Response(songs, status=status.HTTP_200_OK)


# ▶️ Play song (public)
@api_view(['GET'])
@permission_classes([AllowAny])
@measure_latency
def play_song(request, song_id):
    song_url = s.get_song_url(song_id)

    if not song_url:
        return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)

    return st.stream_song(song_url)


# 🔍 Search songs (public)
@api_view(['GET'])
@permission_classes([AllowAny])
def search_song(request):
    song_name = request.query_params.get("title")

    if not song_name:
        return Response(
            {"error": "title query parameter required"},
            status=status.HTTP_400_BAD_REQUEST
        )

    songs = s.get_song_by_title(song_name)

    if not songs:
        return Response(
            {"message": "No songs found"},
            status=status.HTTP_404_NOT_FOUND
        )

    return Response(songs, status=status.HTTP_200_OK)


# ⬆️ Upload song (protected)
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def upload_song(request):
    user = request.user

    response, status_code = u.upload_song(request, user)

    return Response(response, status=status_code)