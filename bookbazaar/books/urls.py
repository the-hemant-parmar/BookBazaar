from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("add/", views.add_book, name="add_book"),
    path("register/", views.register, name="register"),
]
