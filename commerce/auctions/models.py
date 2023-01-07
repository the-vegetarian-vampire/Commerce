from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Category(models.Model):
    categoryName = models.CharField(max_length=64)

    def __str__(self) -> str:
        return self.categoryName

class Auction_Listing(models.Model):
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=164)
    imageURL = models.CharField(max_length=64)
    price = models.FloatField()
    active = models.BooleanField(default=True)
    ower = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null = True, related_name="user")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True, related_name="category")

    def __str__(self) -> str:
        return self.title