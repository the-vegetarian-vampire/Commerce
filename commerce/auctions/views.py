from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import User, Category, Listing, Bid, Comment


def index(request):
    listings = Listing.objects.filter(active=True)
    categories = Category.objects.all()
    return render(request, "auctions/index.html", {
        "listings": listings,
        "categories": categories,
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")

def create_new(request):
    if request.method == "GET":
        categories = Category.objects.all()
        return render(request, "auctions/create_new.html", {
            "categories": categories
        })
    else:
        title = request.POST["title"]
        description = request.POST["description"]
        price = request.POST["price"]
        imageURL = request.POST["image"]
        category = request.POST["category"]
        current_user = request.user

        data = Category.objects.get(categoryName=category)
        bid = Bid(bid=float(price), user=current_user)
        bid.save()

        new_listing = Listing(
            title=title,
            description=description,
            price=bid,
            imageURL=imageURL,
            category=data,
            owner=current_user,
        )
        new_listing.save()
        return HttpResponseRedirect(reverse(index))

def all_categories(request):
    if request.method == "POST":
        categoryform = request.POST['category']
        category = Category.objects.get(categoryName=categoryform)
        listings = Listing.objects.filter(active=True, category=category)
        categories = Category.objects.all()
        return render(request, "auctions/index.html", {
            "listings": listings,
            "categories": categories,
        })

def listing(request, id):
    data = Listing.objects.get(pk=id)
    listing_in_watchlist = request.user in data.watchlist.all()
    all_comments = Comment.objects.filter(listing=data)
    owner = request.user.username == data.owner.username
    return render(request, "auctions/listing.html", {
        "listing": data,
        "listing_in_watchlist": listing_in_watchlist,
        "all_comments": all_comments,
        "owner": owner,
    })

def watchlist(request):
    if request.method == "GET":
        categories = Category.objects.all()
        return render(request, "auctions/watchlist.html", {
            "categories": categories
            })

def remove_watchlist(request, id):
    data = Listing.objects.get(pk=id)
    user = request.user
    data.watchlist.remove(user)
    return HttpResponseRedirect(reverse("listing",args=(id, )))

def add_watchlist(request, id):
    data = Listing.objects.get(pk=id)
    user = request.user
    data.watchlist.add(user)
    return HttpResponseRedirect(reverse("listing",args=(id, )))

def display_watchlist(request):
    c_user = request.user
    listings = c_user.list_watchlist.all() 
    return render(request, "auctions/watchlist.html", {
        "listings": listings,
    })

def categories(request):
    if request.method == "GET":
        categories = Category.objects.all()
        return render(request, "auctions/categories.html", {
            "categories": categories
            })

def add_comment(request, id):
    user = request.user
    data = Listing.objects.get(pk=id)
    message = request.POST['new_comment']

    new_comment = Comment(
        author=user, 
        listing=data,
        message=message
    )
    new_comment.save()
    return HttpResponseRedirect(reverse("listing",args=(id, )))

def new_bid(request, id):
    newbid = request.POST['newbid']
    data = Listing.objects.get(pk=id)
    listing_in_watchlist = request.user in data.watchlist.all()
    all_comments = Comment.objects.filter(listing=data)
    owner = request.user.username == data.owner.username
    if float(newbid) > data.price.bid:
        higher_bid = Bid(user=request.user, bid=float(newbid))
        higher_bid.save()
        data.price = higher_bid
        data.save()
        return render(request, "auctions/listing.html", {
            "listing": data,
            "listing_in_watchlist": listing_in_watchlist,
            "all_comments": all_comments,
            "owner": owner,
            "message": "Bid successful",
            "update": True
            })
    else:
         return render(request, "auctions/listing.html", {
            "listing": data,
            "listing_in_watchlist": listing_in_watchlist,
            "all_comments": all_comments,
            "owner": owner,
            "message": "Bid failed",
            "update": False
            })

def close_auction(request, id):
    data = Listing.objects.get(pk=id)
    data.active = False
    data.save()
    listing_in_watchlist = request.user in data.watchlist.all()
    all_comments = Comment.objects.filter(listing=data)
    owner = request.user.username == data.owner.username
    return render(request, "auctions/listing.html", {
        "listing": data,
        "listing_in_watchlist": listing_in_watchlist,
        "all_comments": all_comments,
        "owner": owner,
        "update": True,
        "message": "Congratulations! Your auction has closed.",
         })

