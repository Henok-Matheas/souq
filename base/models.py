from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE,SET_NULL


class Shop(models.Model):
    host = models.ForeignKey(User, on_delete= models.SET_NULL, null = True)
    name = models.CharField()
    description = models.TextField(null=True, blank=True)
    customers = models.ManyToManyField(User,related_name='customers', blank='true')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    location = models.CharField()

    class Meta:
        ordering = ['-updated','-created']


    def __str__(self):
        return str(self.name)


class Material(models.Model):
    name = models.CharField()
    detail = models.CharField()
    price = models.FloatField()
    quantity = models.IntegerField()
    # owner = models.ForeignKey()
    shop = models.ForeignKey(Shop, on_delete= models.CASCADE)

    def __str__(self):
        return str(self.name)


class Rating(models.Model):
    name = models.CharField()
    bio = models.CharField()
    material = models.ForeignKey(Material, on_delete= models.CASCADE)
    location = models.CharField()

    def __str__(self):
        return self.name

    # customers =