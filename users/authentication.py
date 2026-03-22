from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from users.utils.jwt import decode_token
from users.models import User

class JWTAuthentication(BaseAuthentication):
    def authenticate(self, request):
        auth_header = request.headers.get("Authorization")

        if not auth_header:
            return None

        try:
            token = auth_header.split(" ")[1]
            payload = decode_token(token)

            user = User.objects.get(id=payload['user_id'])
            return (user, None)

        except Exception:
            raise AuthenticationFailed("Invalid token")