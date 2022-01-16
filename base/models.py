from cv2 import CascadeClassifier
from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE, SET_NULL
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from souq import settings


class User(AbstractBaseUser):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField(
        verbose_name="email address",
        max_length=255,
        unique=True,
    )
    is_customer = models.BooleanField(default=False)
    is_seller = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []  # Email & Password are required by default.

    def __str__(self):
        return self.name

    # def has_perm(self, perm, obj=None):
    #     "Does the user have a specific permission?"
    #     # Simplest possible answer: Yes, always
    #     return True

    # def has_module_perms(self, app_label):
    #     "Does the user have permissions to view the app `app_label`?"
    #     # Simplest possible answer: Yes, always
    #     return True

    @property
    def is_customer(self):
        "Is the user a member of staff?"
        return self.is_customer

    @property
    def is_seller(self):
        "Is the user a admin member?"
        return self.is_seller


class Shop(models.Model):
    host = models.ForeignKey(User, models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    customers = models.ManyToManyField(User, related_name="customers", blank="true")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    address = models.CharField(max_length=200)

    class Meta:
        ordering = ["-updated", "-created"]

    def __str__(self):
        return str(self.name)


class Item(models.Model):
    name = models.CharField(max_length=100)
    detail = models.CharField(max_length=500)
    price = models.FloatField()
    quantity = models.IntegerField()
    # owner = models.ForeignKey()
    shop = models.ForeignKey(Shop, models.CASCADE)

    def __str__(self):
        return str(self.name)


class ItemReview(models.Model):
    name = models.CharField(max_length=100)
    comment = models.CharField(max_length=250)
    rating = models.IntegerField()
    Item = models.ForeignKey(Item, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class ShopReview(models.Model):
    name = models.CharField(max_length=100)
    comment = models.CharField(max_length=250)
    rating = models.IntegerField()
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    image = models.ImageField(upload_to="media", null=True)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)


class OrderItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.item.title}"

    def get_total_item_price(self):
        return self.quantity * self.item.price

    def get_final_price(self):
        return self.get_total_item_price()
