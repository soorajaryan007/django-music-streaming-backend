import datetime
import jwt

SECRET_KEY = "your_secret_key"

def generate_token(user):
    now = datetime.datetime.now(datetime.timezone.utc)

    payload = {
        "user_id": user.id,
        "exp": now + datetime.timedelta(hours=24),
        "iat": now
    }

    token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
    return token


def decode_token(token):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return payload
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None