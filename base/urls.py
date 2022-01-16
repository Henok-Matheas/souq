from django.urls import path
from . import views

urlpatterns = [
    path("", views.getRoutes, name="Routes"),
    # user object
    path("users", views.getUsers, name="getUsers"),
    path("user/<str:pk>", views.getUser, name="getUser"),
    # shop object
    path("shops", views.getShops, name="getShops"),
    path("shop<str:pk>", views.getShop, name="getShop"),
    # item object
    path("items", views.getItems, name="getItems"),
    path("item<str:pk>", views.getItem, name="getItem"),
    # item review
    path("itemreviews", views.getItemReviews, name="getItemReviews"),
    path("itemreivew<str:pk>", views.getItemReview, name="getItemReview"),
    # shop review
    path("shopreviews", views.getShopReviews, name="getShopReviews"),
    path("shopreview<str:pk>", views.getShopReview, name="getShopReview"),
    # path("create", views.create, name="create"),
]
