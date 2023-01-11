from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Category(models.Model):
    categoryName = models.CharField(max_length=64)

    def __str__(self) -> str:
        return self.categoryName

class Bid(models.Model):
    bid = models.DecimalField(default=0, max_digits=6, decimal_places=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_bid")

    def num_bids(self):
        return self.bids.all()

class Listing(models.Model):
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=280)
    price = models.ForeignKey(Bid, on_delete=models.CASCADE, blank=True, null=True, related_name="bid_price")
    imageURL = models.CharField(max_length=1000)
    active = models.BooleanField(default=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null = True, related_name="user")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True, related_name="category")
    watchlist = models.ManyToManyField(User, blank=True, null=True, related_name="list_watchlist")
    time = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title


class Comment(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, blank=True, null=True, related_name="listing_comment")
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="user_comment")
    message = models.CharField(max_length=280)
    time = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.author} comment on {self.listing}"