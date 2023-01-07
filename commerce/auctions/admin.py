from django.contrib import admin
from .models import Auction_Listing, User, Category

# Register your models here.
admin.site.register(Auction_Listing)
admin.site.register(User)
admin.site.register(Category)