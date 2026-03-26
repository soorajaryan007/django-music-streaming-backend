import logging
import json

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import status

from songs.services.song_service import SongService
from songs.services.song_upload import SongController
from songs.utils.response_handler import StreamingService
from songs.api_latency.latency import measure_latency

from groq import Groq

logger = logging.getLogger(__name__)

s = SongService()
u = SongController()
st = StreamingService()

# Initialize Groq client
client = Groq(api_key="YOUR_GROQ_API_KEY")


# -------------------------------
# 🎵 Get all songs (public)
# -------------------------------
@api_view(['GET'])
@permission_classes([AllowAny])
def get_songs(request):
    songs = s.get_all_songs()
    return Response(songs, status=status.HTTP_200_OK)


# -------------------------------
# ▶️ Play song (public)
# -------------------------------
@api_view(['GET'])
@permission_classes([AllowAny])
@measure_latency
def play_song(request, song_id):
    song_url = s.get_song_url(song_id)

    if not song_url:
        return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)

    return st.stream_song(song_url)


# -------------------------------
# 🔍 Search songs (v1 - keyword)
# -------------------------------
@api_view(['GET'])
@permission_classes([AllowAny])
def search_song(request):
    song_name = request.query_params.get("q")

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

    return Response({
        "version": "v1",
        "results": songs
    }, status=status.HTTP_200_OK)


# -------------------------------
# 🧠 Natural Language Parser (Groq)
# -------------------------------
def parse_query(query):
    try:
        prompt = f"""
        Extract filters from this music search query:
        "{query}"

        Return ONLY valid JSON with keys:
        title, artist, genre, mood, year

        If not present, use null.
        """

        response = client.chat.completions.create(
            model="llama3-70b-8192",  # fast + powerful
            messages=[{"role": "user", "content": prompt}],
            temperature=0
        )

        content = response.choices[0].message.content.strip()

        # Ensure valid JSON parsing
        return json.loads(content)

    except Exception as e:
        logger.error(f"Groq parsing failed: {e}")

        # Fallback: treat whole query as title search
        return {
            "title": query,
            "artist": None,
            "genre": None,
            "mood": None,
            "year": None
        }


# -------------------------------
# 🔍 Natural Search (v2 - AI)
# -------------------------------
@api_view(['GET'])
@permission_classes([AllowAny])
def natural_search_song(request):
    query = request.query_params.get("q")

    if not query:
        return Response(
            {"error": "q parameter required"},
            status=status.HTTP_400_BAD_REQUEST
        )

    # ⚡ Optimization: skip LLM for simple queries
    if len(query.split()) <= 2:
        filters = {
            "title": query,
            "artist": None,
            "genre": None,
            "mood": None,
            "year": None
        }
    else:
        filters = parse_query(query)

    songs = s.get_song_by_natural_query(filters)


    if not songs:
        return Response(
            {"message": "No songs found"},
            status=status.HTTP_404_NOT_FOUND
        )

    return Response({
        "version": "v2",
        "query": query,
        "interpreted_filters": filters,
        "results_count": len(songs),
        "results": songs
    }, status=status.HTTP_200_OK)


# -------------------------------
# ⬆️ Upload song (protected)
# -------------------------------
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def upload_song(request):
    user = request.user

    response, status_code = u.upload_song(request, user)

    return Response(response, status=status_code)