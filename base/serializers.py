from ast import Mod
from rest_framework.serializers import ModelSerializer
from .models import *


class UserSerializer(ModelSerializer):
    Model = User
    fields = "__all__"


class ShopSerializer(ModelSerializer):
    Model = Shop
    fields = "__all__"


class ItemSerializer(ModelSerializer):
    Model = User
    fields = "__all__"


class ItemReviewSerializer(ModelSerializer):
    Model = User
    fields = "__all__"


class ShopReviewSerializer(ModelSerializer):
    Model = User
    fields = "__all__"


class ProductImageSerializer(ModelSerializer):
    Model = User
    fields = "__all__"


class OrderItemSerializer(ModelSerializer):
    Model = User
    fields = "__all__"
