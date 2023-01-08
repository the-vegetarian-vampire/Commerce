from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create", views.create_new, name="create"),
    path("watchlist", views.watchlist, name="watchlist"),
    path("categories", views.categories, name="categories"),
    path("all_categories", views.all_categories, name="all_categories"),
    path("listing/<int:id>", views.listing, name="listing"),
    path("removeWatchlist/<int:id>", views.removeWatchlist, name="removeWatchlist"),
    path("addWatchlist/<int:id>", views.addWatchlist, name="addWatchlist"),
    path("watchlist/<int:id>", views.display_watchlist, name="watchlist"),

]
