from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

from base.models import *
from base.serializers import *

from base.utils import *

# Create your views here.


@api_view(["GET"])
def getRoutes(request):
    routes = [
        # user
        {
            "Endpoint": "/users/",
            "method": "GET",
            "body": None,
            "description": "Returns an array of users",
        },
        {
            "Endpoint": "/users/id",
            "method": "GET",
            "body": None,
            "description": "Returns a single user object",
        },
        {
            "Endpoint": "/users/create/",
            "method": "POST",
            "body": {"body": ""},
            "description": "Creates new user with data sent in post request",
        },
        {
            "Endpoint": "/users/id/update/",
            "method": "PUT",
            "body": {"body": ""},
            "description": "Creates an existing user with data sent in post request",
        },
        {
            "Endpoint": "/users/id/delete/",
            "method": "DELETE",
            "body": None,
            "description": "Deletes and exiting user",
        },
        # Shop
        {
            "Endpoint": "/shops/",
            "method": "GET",
            "body": None,
            "description": "Returns an array of shops",
        },
        {
            "Endpoint": "/shops/id",
            "method": "GET",
            "body": None,
            "description": "Returns a single shop object",
        },
        {
            "Endpoint": "/shops/create/",
            "method": "POST",
            "body": {"body": ""},
            "description": "Creates new shops with data sent in post request",
        },
        {
            "Endpoint": "/shops/id/update/",
            "method": "PUT",
            "body": {"body": ""},
            "description": "Creates an existing shops with data sent in post request",
        },
        {
            "Endpoint": "/shops/id/delete/",
            "method": "DELETE",
            "body": None,
            "description": "Deletes and exiting shops",
        },
        # items
        {
            "Endpoint": "/items/",
            "method": "GET",
            "body": None,
            "description": "Returns an array of items",
        },
        {
            "Endpoint": "/items/id",
            "method": "GET",
            "body": None,
            "description": "Returns a single item object",
        },
        {
            "Endpoint": "/items/create/",
            "method": "POST",
            "body": {"body": ""},
            "description": "Creates new item with data sent in post request",
        },
        {
            "Endpoint": "/items/id/update/",
            "method": "PUT",
            "body": {"body": ""},
            "description": "Creates an existing item with data sent in post request",
        },
        {
            "Endpoint": "/items/id/delete/",
            "method": "DELETE",
            "body": None,
            "description": "Deletes and exiting item",
        },
        # item review
        {
            "Endpoint": "/itemReviews/",
            "method": "GET",
            "body": None,
            "description": "Returns an array of itemReviews",
        },
        {
            "Endpoint": "/itemReviews/id",
            "method": "GET",
            "body": None,
            "description": "Returns a single itemReview object",
        },
        {
            "Endpoint": "/itemReviews/create/",
            "method": "POST",
            "body": {"body": ""},
            "description": "Creates new itemReview with data sent in post request",
        },
        {
            "Endpoint": "/itemReviews/id/update/",
            "method": "PUT",
            "body": {"body": ""},
            "description": "Creates an existing itemReview with data sent in post request",
        },
        {
            "Endpoint": "/itemReviews/id/delete/",
            "method": "DELETE",
            "body": None,
            "description": "Deletes and exiting itemReview",
        },
        # shop review
        {
            "Endpoint": "/shopReviews/",
            "method": "GET",
            "body": None,
            "description": "Returns an array of shopReviews",
        },
        {
            "Endpoint": "/shopReviews/id",
            "method": "GET",
            "body": None,
            "description": "Returns a single shopReview object",
        },
        {
            "Endpoint": "/shopReviews/create/",
            "method": "POST",
            "body": {"body": ""},
            "description": "Creates new shopReview with data sent in post request",
        },
        {
            "Endpoint": "/shopReviews/id/update/",
            "method": "PUT",
            "body": {"body": ""},
            "description": "Creates an existing shopReview with data sent in post request",
        },
        {
            "Endpoint": "/shopReviews/id/delete/",
            "method": "DELETE",
            "body": None,
            "description": "Deletes and exiting shopReview",
        },
        # order item
        {
            "Endpoint": "/orderItems/",
            "method": "GET",
            "body": None,
            "description": "Returns an array of orderItems",
        },
        {
            "Endpoint": "/orderItems/id",
            "method": "GET",
            "body": None,
            "description": "Returns a single orderItems object",
        },
        {
            "Endpoint": "/orderItems/create/",
            "method": "POST",
            "body": {"body": ""},
            "description": "Creates new orderItems with data sent in post request",
        },
        {
            "Endpoint": "/orderItems/id/update/",
            "method": "PUT",
            "body": {"body": ""},
            "description": "Creates an existing orderItems with data sent in post request",
        },
        {
            "Endpoint": "/orderItems/id/delete/",
            "method": "DELETE",
            "body": None,
            "description": "Deletes and exiting orderItem",
        },
    ]

    return Response(routes)


############################## USER OBJECT #############################
@api_view(["GET", "POST"])
def getUsers(request):

    if request.method == "GET":
        return getUsersList(request)

    if request.method == "POST":
        return createUser(request)


@api_view(["GET", "PUT", "DELETE"])
def getUser(request, pk):

    if request.method == "GET":
        return getUserDetail(request, pk)

    if request.method == "PUT":
        return updateUser(request, pk)

    if request.method == "DELETE":
        return deleteUser(request, pk)


# @api_view(["GET"])
# def getUsers(request):
#     users = User.objects.all()
#     userSerialized = UserSerializer(users, many=True)

#     return Response(userSerialized.data)
#     # shop
#     shops = Shop.objects.all()
#     shopSerializer = ShopSerializer(shops, many=True)

#     # shopReview
#     shopReviews = ShopReview.objects.all()
#     shopReviewSerializer = ShopReviewSerializer(shopReviews, many=True)

#     # item
#     items = Item.objects.all()
#     itemSerializer = Serializer(shops, many=True)

#     itemReviews = ItemReview.objects.all()

#     return Response()


# @api_view(["GET"])
# def getShops(request):
#     # shop
#     shops = Shop.objects.all()
#     shopSerializer = ShopSerializer(shops, many=True)

#     # shopReview
#     shopReviews = ShopReview.objects.all()
#     shopReviewSerializer = ShopReviewSerializer(shopReviews, many=True)

#     # item
#     items = Item.objects.all()
#     itemSerializer = ItemSerializer(shops, many=True)

#     itemReviews = ItemReview.objects.all()

#     return Response()


# def getItems(request):
#     # shop
#     shops = Shop.objects.all()
#     shopSerializer = ShopSerializer(shops, many=True)

#     # shopReview
#     shopReviews = ShopReview.objects.all()
#     shopReviewSerializer = ShopReviewSerializer(shopReviews, many=True)

#     # item
#     items = Item.objects.all()
#     itemSerializer = ItemSerializer(shops, many=True)

#     itemReviews = ItemReview.objects.all()

#     return Response()


# @api_view(["GET"])
# def getItemReview(request):
#     # shop
#     shops = Shop.objects.all()
#     shopSerializer = ShopSerializer(shops, many=True)

#     # shopReview
#     shopReviews = ShopReview.objects.all()
#     shopReviewSerializer = ShopReviewSerializer(shopReviews, many=True)

#     # item
#     items = Item.objects.all()
#     itemSerializer = ItemSerializer(shops, many=True)

#     itemReviews = ItemReview.objects.all()

#     return Response()


# @api_view(["GET"])
# def getShopReview(request):
#     # shop
#     shops = Shop.objects.all()
#     shopSerializer = ShopSerializer(shops, many=True)

#     # shopReview
#     shopReviews = ShopReview.objects.all()
#     shopReviewSerializer = ShopReviewSerializer(shopReviews, many=True)

#     # item
#     items = Item.objects.all()
#     itemSerializer = ItemSerializer(shops, many=True)

#     itemReviews = ItemReview.objects.all()

#     return Response()


# @api_view(["GET"])
# def getProductImage(request):
#     # shop
#     shops = Shop.objects.all()
#     shopSerializer = ShopSerializer(shops, many=True)

#     # shopReview
#     shopReviews = ShopReview.objects.all()
#     shopReviewSerializer = ShopReviewSerializer(shopReviews, many=True)

#     # item
#     items = Item.objects.all()
#     itemSerializer = ItemSerializer(shops, many=True)

#     itemReviews = ItemReview.objects.all()

#     return Response()


# @api_view(["GET"])
# def getOrderItem(request):
#     # shop
#     shops = Shop.objects.all()
#     shopSerializer = ShopSerializer(shops, many=True)

#     # shopReview
#     shopReviews = ShopReview.objects.all()
#     shopReviewSerializer = ShopReviewSerializer(shopReviews, many=True)

#     # item
#     items = Item.objects.all()
#     itemSerializer = ItemSerializer(shops, many=True)

#     itemReviews = ItemReview.objects.all()

#     return Response()
