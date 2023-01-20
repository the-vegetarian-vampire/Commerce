from django.contrib import admin
from .models import Listing, User, Category, Bid, Comment

# Register your models here.
class ListingAdmin(admin.ModelAdmin):
    list_display = ("id", "owner", "title", "price", "time")

class BidAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "bid", "listing", "time")

class CommentAdmin(admin.ModelAdmin):
    list_display = ("id", "listing", "author", "message", "time")

admin.site.register(Listing, ListingAdmin)
admin.site.register(User)
admin.site.register(Category)
admin.site.register(Bid, BidAdmin)
admin.site.register(Comment, CommentAdmin)