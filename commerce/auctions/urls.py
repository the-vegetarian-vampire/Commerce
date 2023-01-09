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
    path("remove_watchlist/<int:id>", views.remove_watchlist, name="remove_watchlist"),
    path("add_watchlist/<int:id>", views.add_watchlist, name="add_watchlist"),
    path("display_watchlist", views.display_watchlist, name="display_watchlist"),
    path("add_comment/<int:id>", views.add_comment, name="add_comment"),

]
