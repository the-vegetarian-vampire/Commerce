from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Category(models.Model):
    categoryName = models.CharField(max_length=64)

    def __str__(self) -> str:
        return self.categoryName

class Listing(models.Model):
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=280)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    imageURL = models.CharField(max_length=1000)
    active = models.BooleanField(default=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null = True, related_name="user")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True, related_name="category")
    watchlist = models.ManyToManyField(User, blank=True, null=True, related_name="list_watchlist")
    time = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title

class Bid(models.Model):
    item = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="bids")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bids")
    number = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return str(self.number)

class Comment(models.Model):
    item = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="user_comment")
    comment = models.CharField(max_length=280)
    time = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.author} comment on {self.item}"