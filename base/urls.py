from django.urls import path
from . import views

urlpatterns = [
    path("", views.getRoutes, name="Routes"),
    path("users", views.getUsers, name="getUsers"),
    # path("create", views.create, name="create"),
]
