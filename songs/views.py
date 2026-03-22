from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_GET, require_POST
from django.views.decorators.csrf import csrf_exempt

from songs.services.song_service import SongService
from songs.services.song_upload import SongController
from songs.utils.response_handler import StreamingService
from songs.api_latency.latency import measure_latency

s = SongService()
u = SongController()
st = StreamingService()


@require_GET
def get_songs(request):
    songs = s.get_all_songs()
    return JsonResponse(songs, safe=False)


@measure_latency
def play_song(request, song_id):
    song_url = s.get_song_url(song_id)
    print("Song URL:", song_url)
    if not song_url:
        return JsonResponse({"error": "Not found"}, status=404)

    return st.stream_song(song_url)


def search_song(request):
    song_name = request.GET.get("title")

    if not song_name:
        return JsonResponse({"error": "title query parameter required"}, status=400)

    songs = s.get_song_by_title(song_name)

    if not songs:
        return JsonResponse({"message": "No songs found"}, status=404)

    return JsonResponse(songs, safe=False)


from django.http import JsonResponse

@csrf_exempt
@require_POST
def upload_song(request):
    response, status = u.upload_song(request)
    return JsonResponse(response, status=status)


def get_users(request):
    users = s.get_all_users()
    return JsonResponse(users, safe=False)