from operator import itemgetter
from rest_framework.response import Response
from .models import *
from .serializers import *


############################# USER OBJECT #############################
def getUsersList(request):
    users = Member.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)


def getUserDetail(request, pk):
    user = Member.objects.get(id=pk)
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)


def createUser(request):
    data = request.user
    user = Member.objects.create(data=request.data)

    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)


def updateUser(request, pk):
    data = request.data
    user = Member.objects.get(id=pk)
    serializer = UserSerializer(instance=user, data=data)

    if serializer.is_valid():
        serializer.save()

    return serializer.data


def deleteUser(request, pk):
    user = Member.objects.get(id=pk)
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
    shop = Shop.objects.create(data=request.data)
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
    item = Item.objects.create(data=request.data)
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
    itemReview = ItemReview.objects.create(data=request.data)
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
    shopReview = ShopReview.objects.create(
        body=data["body"],
    )
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


############################# ORDERITEM OBJECT #############################
def getOrderItemList(request):
    orderItems = OrderItem.objects.all()
    serializer = OrderItemSerializer(orderItems, many=True)
    return Response(serializer.data)


def getOrderItemDetail(request, pk):
    orderItem = OrderItem.objects.get(id=pk)
    serializer = OrderItemSerializer(orderItem, many=False)
    return Response(serializer.data)


def createOrderItem(request):
    data = request.data
    orderItem = OrderItem.objects.create(body=data["body"])
    serializer = OrderItemSerializer(orderItem, many=False)
    return Response(serializer.data)


def updateOrderItem(request, pk):
    data = request.data
    orderItem = OrderItem.objects.get(id=pk)
    serializer = OrderItemSerializer(instance=orderItem, data=data)

    if serializer.is_valid():
        serializer.save()

    return serializer.data


def deleteOrderItem(request, pk):
    orderItem = OrderItem.objects.get(id=pk)
    orderItem.delete()
    return Response("Note was deleted!")
