from operator import itemgetter
from rest_framework.response import Response
from .models import *
from .serializers import *


############################# USER OBJECT #############################
def getUsersList(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)


def getUserDetail(request, pk):
    user = User.objects.get(id=pk)
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)


def createUser(request):
    data = request.data
    user = User.objects.create(body=data["body"])
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)


def updateUser(request, pk):
    data = request.data
    user = User.objects.get(id=pk)
    serializer = UserSerializer(instance=user, data=data)

    if serializer.is_valid():
        serializer.save()

    return serializer.data


def deleteUser(request, pk):
    user = User.objects.get(id=pk)
    user.delete()
    return Response("Note was deleted!")


############################# SHOP OBJECT #############################
def getShopsList(request):
    shops = Shop.objects.all()
    serializer = ShopSerializer(shops, many=True)
    return Response(serializer.data)


def getShopDetail(request, pk):
    shop = Shop.objects.get(id=pk)
    serializer = ShopSerializer(shop, many=False)
    return Response(serializer.data)


def createShop(request):
    data = request.data
    shop = Shop.objects.create(body=data["body"])
    serializer = ShopSerializer(shop, many=False)
    return Response(serializer.data)


def updateShop(request, pk):
    data = request.data
    shop = Shop.objects.get(id=pk)
    serializer = ShopSerializer(instance=Shop, data=data)

    if serializer.is_valid():
        serializer.save()

    return serializer.data


def deleteShop(request, pk):
    shop = Shop.objects.get(id=pk)
    shop.delete()
    return Response("Note was deleted!")


############################# ITEM OBJECT #############################
def getItemsList(request):
    items = Item.objects.all()
    serializer = ItemSerializer(items, many=True)
    return Response(serializer.data)


def getItemDetail(request, pk):
    item = Item.objects.get(id=pk)
    serializer = UserSerializer(item, many=False)
    return Response(serializer.data)


def createItem(request):
    data = request.data
    item = Item.objects.create(body=data["body"])
    serializer = ItemSerializer(item, many=False)
    return Response(serializer.data)


def updateItem(request, pk):
    data = request.data
    item = Item.objects.get(id=pk)
    serializer = ItemSerializer(instance=item, data=data)

    if serializer.is_valid():
        serializer.save()

    return serializer.data


def deleteItem(request, pk):
    item = Item.objects.get(id=pk)
    item.delete()
    return Response("Note was deleted!")


############################# ItemReview OBJECT #############################
def getItemReviewList(request):
    itemReviews = ItemReview.objects.all()
    serializer = ItemReviewSerializer(itemReviews, many=True)
    return Response(serializer.data)


def getItemReviewDetail(request, pk):
    itemReview = ItemReview.objects.get(id=pk)
    serializer = ItemReviewSerializer(itemReview, many=False)
    return Response(serializer.data)


def createItemReview(request):
    data = request.data
    itemReview = ItemReview.objects.create(body=data["body"])
    serializer = ItemReviewSerializer(itemReview, many=False)
    return Response(serializer.data)


def updateItemReview(request, pk):
    data = request.data
    itemReview = ItemReview.objects.get(id=pk)
    serializer = ItemReviewSerializer(instance=itemReview, data=data)

    if serializer.is_valid():
        serializer.save()

    return serializer.data


def deleteItemReview(request, pk):
    itemReview = ItemReview.objects.get(id=pk)
    itemReview.delete()
    return Response("Note was deleted!")


############################# ShopReview OBJECT #############################
def getShopReviewList(request):
    shopReviews = ShopReview.objects.all()
    serializer = ShopReviewSerializer(shopReviews, many=True)
    return Response(serializer.data)


def getShopReviewDetail(request, pk):
    shopReview = ShopReview.objects.get(id=pk)
    serializer = ShopReviewSerializer(shopReview, many=False)
    return Response(serializer.data)


def createShopReview(request):
    data = request.data
    shopReview = ShopReview.objects.create(body=data["body"])
    serializer = ShopReviewSerializer(shopReview, many=False)
    return Response(serializer.data)


def updateShopReview(request, pk):
    data = request.data
    shopReview = ShopReview.objects.get(id=pk)
    serializer = ShopReviewSerializer(instance=shopReview, data=data)

    if serializer.is_valid():
        serializer.save()

    return serializer.data


def deleteShopReview(request, pk):
    shopReview = ShopReview.objects.get(id=pk)
    shopReview.delete()
    return Response("Note was deleted!")


# ############################# ORDERITEM OBJECT #############################
# def getOrderItemList(request):
#     orderItems = OrderItem.objects.all()
#     serializer = OrderItemSerializer(orderItems, many=True)
#     return Response(serializer.data)


# def getOrderItemDetail(request, pk):
#     user = User.objects.get(id=pk)
#     serializer = UserSerializer(user, many=False)
#     return Response(serializer.data)


# def createUser(request):
#     data = request.data
#     user = User.objects.create(body=data["body"])
#     serializer = UserSerializer(user, many=False)
#     return Response(serializer.data)


# def updateUser(request, pk):
#     data = request.data
#     user = User.objects.get(id=pk)
#     serializer = UserSerializer(instance=user, data=data)

#     if serializer.is_valid():
#         serializer.save()

#     return serializer.data


# def deleteUser(request, pk):
#     user = User.objects.get(id=pk)
#     user.delete()
#     return Response("Note was deleted!")
