from ast import Mod
from rest_framework.serializers import ModelSerializer
from .models import *


class UserSerializer(ModelSerializer):
    class Meta:
        model = Member
        fields = "__all__"


class ShopSerializer(ModelSerializer):
    model = Shop
    fields = "__all__"


class ItemSerializer(ModelSerializer):
    class Meta:
        model = Item
        fields = "__all__"


class ItemReviewSerializer(ModelSerializer):
    model = ItemReview
    fields = "__all__"


class ShopReviewSerializer(ModelSerializer):
    model = ShopReview
    fields = "__all__"


class ProductImageSerializer(ModelSerializer):
    model = ProductImage
    fields = "__all__"


class OrderItemSerializer(ModelSerializer):
    model = OrderItem
    fields = "__all__"
