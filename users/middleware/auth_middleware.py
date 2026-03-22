from django.http import JsonResponse
from users.utils.jwt import decode_token
from users.models import User

class JWTAuthenticationMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        auth_header = request.headers.get("Authorization")

        if auth_header:
            try:
                token = auth_header.split(" ")[1]  # Bearer <token>
                payload = decode_token(token)

                if payload:
                    user = User.objects.filter(id=payload["user_id"]).first()
                    request.user = user
                else:
                    return JsonResponse({"error": "Invalid or expired token"}, status=401)

            except Exception:
                return JsonResponse({"error": "Invalid token format"}, status=401)

        else:
            request.user = None

        return self.get_response(request)