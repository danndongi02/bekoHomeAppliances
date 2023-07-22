from django.contrib import admin
from django.urls import path

from core.views import homepage, shop
from product.views import product

urlpatterns = [
    path("", homepage, name="homepage"),
    path("shop/", shop, name="shop"),
    path("product/", product, name="product"),
    path('admin/', admin.site.urls),
]
