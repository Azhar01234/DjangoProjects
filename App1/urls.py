from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("<int:x>", views.flight, name="flight"),
    path("<int:x>/book", views.book, name="book")
]