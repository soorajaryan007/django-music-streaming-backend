import logging

from django.contrib.auth.hashers import check_password
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import status

from users.models import User
from users.serializers import RegisterSerializer, LoginSerializer
from users.utils.jwt import generate_token

logger = logging.getLogger(__name__)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_users(request):
    users = User.objects.all()[:20]

    data = [
        {"id": u.id, "username": u.username, "email": u.email}
        for u in users
    ]

    return Response(data, status=status.HTTP_200_OK)


@api_view(['POST'])
def register_user(request):
    serializer = RegisterSerializer(data=request.data)

    if not serializer.is_valid():
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    user = serializer.save()

    return Response({
        "message": "User registered successfully",
        "user_id": user.id
    }, status=status.HTTP_201_CREATED)


@api_view(['POST'])
def login_user(request):
    serializer = LoginSerializer(data=request.data)

    if not serializer.is_valid():
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    email = serializer.validated_data['email']
    password = serializer.validated_data['password']

    user = User.objects.filter(email=email).first()

    if not user or not check_password(password, user.password):
        return Response(
            {"error": "Invalid credentials"},
            status=status.HTTP_401_UNAUTHORIZED
        )

    token = generate_token(user)

    return Response({
        "message": "Login successful",
        "token": token
    }, status=status.HTTP_200_OK)