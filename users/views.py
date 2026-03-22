import json

from django.http import JsonResponse
from django.contrib.auth.hashers import make_password, check_password
from django.views.decorators.csrf import csrf_exempt

from users.models import User
from users.utils.jwt import generate_token

def get_users(request):
    users = User.objects.all()[:20]

    data = [
        {"id": u.id, "username": u.username, "email": u.email}
        for u in users
    ] 

    return JsonResponse(data, safe=False)



@csrf_exempt
def register_user(request):
    if request.method != "POST":
        return JsonResponse({"error": "Only POST allowed"}, status=405)

    try:
        body = json.loads(request.body)

        username = body.get("username")
        email = body.get("email")
        password = body.get("password")

        if not username or not email or not password:
            return JsonResponse({"error": "All fields required"}, status=400)

        if User.objects.filter(email=email).exists():
            return JsonResponse({"error": "Email already exists"}, status=400)

        user = User.objects.create(
            username=username,
            email=email,
            password=make_password(password)  # 🔥 hashed
        )

        return JsonResponse({
            "message": "User registered successfully",
            "user_id": user.id
        })

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)
    


@csrf_exempt
def login_user(request):
    if request.method != "POST":
        return JsonResponse({"error": "Only POST allowed"}, status=405)

    try:
        body = json.loads(request.body)

        email = body.get("email")
        password = body.get("password")

        user = User.objects.filter(email=email).first()

        if not user:
            return JsonResponse({"error": "User not found"}, status=404)

        if not check_password(password, user.password):
            return JsonResponse({"error": "Invalid password"}, status=400)

        token = generate_token(user)

        return JsonResponse({
            "message": "Login successful",
            "token": token
        })

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)