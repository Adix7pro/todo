from django.urls import path, include
from . import views


urlpatterns = [
    path("register", views.register_request, name="register"),
    path("login", views.loginView, name="login"),
    path("logout", views.logout_view, name="logout")
]