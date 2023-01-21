from django.urls import path
from shop import views

urlpatterns = [
    path("", views.index, name='ShopHome'),
    path("tracker/", views.tracker, name='ShopTracker'),
    path("about/", views.about, name='ShopAbout'),
    path("contact/", views.contact, name='ShopContact'),
    path("search/", views.search, name='ShopSearch'),
    path("checkout/", views.checkout, name='ShopCheckout'),
    path("product/<int:myid>", views.productView, name="ShopProductView"),
]
