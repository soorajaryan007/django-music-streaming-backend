from django.urls import path
from users.views import register_user, get_users, login_user

urlpatterns = [
    path("register/", register_user),
    path("users/", get_users),
    path("login/", login_user),
]