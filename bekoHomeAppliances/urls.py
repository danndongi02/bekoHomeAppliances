from django.contrib import admin
from django.urls import path

from core.views import homepage, shop

urlpatterns = [
    path("", homepage, name="homepage"),
    path("shop/", shop, name="shop"),
    path('admin/', admin.site.urls),
]
