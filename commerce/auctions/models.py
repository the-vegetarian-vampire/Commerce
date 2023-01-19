from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import Max


class User(AbstractUser):
    pass

class Category(models.Model):
    categoryName = models.CharField(max_length=64)
   
    class Meta:
        ordering = ('categoryName',)

    def __str__(self) -> str:
        return self.categoryName


class Listing(models.Model):
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=280)
    price = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    bid_count = models.IntegerField(default=0)
    imageURL = models.CharField(max_length=1000)
    active = models.BooleanField(default=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null = True, related_name="user")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True, related_name="category")
    watchlist = models.ManyToManyField(User, blank=True, null=True, related_name="list_watchlist")
    time = models.DateTimeField(auto_now_add=True)
    winner = models.ForeignKey(User, on_delete=models.SET_NULL, default=None, blank=True, null=True, related_name="winning_user")

    def __str__(self):
        return self.title
    
    def num_bids(self):
        return self.bids.all().count()

    def current_price(self):
        if self.num_bids() > 0:
            return round(self.bids.aggregate(Max('bid'))['bid__max'],2)
        else: 
            return self.price

class Bid(models.Model):
    bid = models.DecimalField(default=0, max_digits=8, decimal_places=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bids")
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, blank=True, null = True, related_name="bids")
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} bid {self.bid} on {self.listing}"

class Comment(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, blank=True, null=True, related_name="listing_comment")
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="user_comment")
    message = models.CharField(max_length=280)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.author} comment on {self.listing}"