from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("more_about", views.read_more_about, name="more_about"),
    path("more_hero", views.read_more_hero, name="more_hero"),
    path("more_service/<str:pk>", views.read_more_service, name="more_service")
]