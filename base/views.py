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


############################## Shop OBJECT #############################
@api_view(["GET", "POST"])
def getShops(request):

    if request.method == "GET":
        return getShopsList(request)

    if request.method == "POST":
        return createShop(request)


@api_view(["GET", "PUT", "DELETE"])
def getShop(request, pk):

    if request.method == "GET":
        return getShopDetail(request, pk)

    if request.method == "PUT":
        return updateShop(request, pk)

    if request.method == "DELETE":
        return deleteShop(request, pk)


############################## Item OBJECT #############################
@api_view(["GET", "POST"])
def getItems(request):

    if request.method == "GET":
        return getItemsList(request)

    if request.method == "POST":
        return createItem(request)


@api_view(["GET", "PUT", "DELETE"])
def getItem(request, pk):

    if request.method == "GET":
        return getItemDetail(request, pk)

    if request.method == "PUT":
        return updateItem(request, pk)

    if request.method == "DELETE":
        return deleteItem(request, pk)


############################## Item Review OBJECT #############################
@api_view(["GET", "POST"])
def getItemReviews(request):

    if request.method == "GET":
        return getItemReviewList(request)

    if request.method == "POST":
        return createItemReview(request)


@api_view(["GET", "PUT", "DELETE"])
def getItemReview(request, pk):

    if request.method == "GET":
        return getItemReviewDetail(request, pk)

    if request.method == "PUT":
        return updateItemReview(request, pk)

    if request.method == "DELETE":
        return deleteItemReview(request, pk)


##############################  Shop Review OBJECT #############################
@api_view(["GET", "POST"])
def getShopReviews(request):

    if request.method == "GET":
        return getShopReviewList(request)

    if request.method == "POST":
        return createShopReview(request)


@api_view(["GET", "PUT", "DELETE"])
def getShopReview(request, pk):

    if request.method == "GET":
        return getShopReviewDetail(request, pk)

    if request.method == "PUT":
        return updateShopReview(request, pk)

    if request.method == "DELETE":
        return deleteShopReview(request, pk)


############################## ORDER ITEMS OBJECT #############################
@api_view(["GET", "POST"])
def getOrderItems(request):

    if request.method == "GET":
        return getOrderItemList(request)

    if request.method == "POST":
        return createOrderItem(request)


@api_view(["GET", "PUT", "DELETE"])
def getOrderItem(request, pk):

    if request.method == "GET":
        return getOrderItemDetail(request, pk)

    if request.method == "PUT":
        return updateOrderItem(request, pk)

    if request.method == "DELETE":
        return deleteOrderItem(request, pk)
