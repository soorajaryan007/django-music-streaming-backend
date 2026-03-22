from django.http import JsonResponse
from users.models import User

def get_users(request):
    users = User.objects.all()[:20]

    data = [
        {"id": u.id, "username": u.username, "email": u.email}
        for u in users
    ]

    return JsonResponse(data, safe=False)